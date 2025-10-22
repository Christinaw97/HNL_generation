import numpy as np
import subprocess
import time
import psutil
import os

# Configuration
max_parallel = 3        # number of parallel jobs
min_free_gb = 2.0       # minimum free memory before starting new job
log_dir = "logs"        # directory to store logs

os.makedirs(log_dir, exist_ok=True)

running = []

for decay in ["e", "mu", "tau"]:
    for m in np.arange(1.0,1.4,0.5):
        m_str = str(m).replace('.','p')
        for coupling in [0.01]:
            name = f"HNL_{decay}_mN_{m_str}_coupling_0p01_13p6TeV"
            log_file = os.path.join(log_dir, f"{name}.log")

            cmd = [
                "python3", "create_gridpack.py",
                "-o", name,
                "--name", name,
                "--massHNL", str(m),
                f"--V{decay}", str(coupling),
                "--majorana",
                "--skipClone"
            ]

            # Wait if too many jobs or not enough memory
            while (
                len(running) >= max_parallel or
                psutil.virtual_memory().available < min_free_gb * 1024**3
            ):
                for p in running[:]:
                    if p.poll() is not None:
                        running.remove(p)
                time.sleep(5)

            print(f"Starting {name} → logging to {log_file}")

            # Open the log file and redirect both stdout and stderr
            with open(log_file, "w") as f:
                p = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
                running.append(p)

# Wait for all jobs to finish
for p in running:
    p.wait()

print(" All jobs finished. Logs are in the 'logs/' directory.")

