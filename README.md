# HNL generation

everything done on cmslpc el8

### Setup
```bash
git clone git@github.com:Christinaw97/HNL_generation.git
cd HNL_generation
git clone https://gitlab.cern.ch/cms-gen/genproductions_scripts.git

```
### Gridpacks Generation
Run `python3 wrapper_create_gridpack_parallel.py` to generate gridpacks for all flavor, mass, and ctau. Job logs saved in `logs`
To check if the gridpacks were created successfully:
```bash
cd scripts
python3 check_logs.py ../logs
```

#### Initial gridpacks run (Doesn't need to be repeated by everyone, to get coupling to ctau relationship)
* Generated gridpacks for all flavor and mass combination at one coupling to know the relationship between the three variables
* Run `python3 scripts/get_width_xsec.py` to generate `data/decay_results.csv` storing all the info
* Functions in `scripts/utilities.py` make use of the csv file

### Plotting script ###
* Plot xsec vs ctau for different masses: `python3 scripts/plot_xsec.py`
