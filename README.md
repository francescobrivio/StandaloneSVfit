## StandaloneSVfit
SVfit implementation for running on ROOT DataFrames.

### Download instructions
```
cmsrel CMSSW_13_0_10
cd CMSSW_13_0_10/src
git clone https://github.com/LLRCMS/ClassicSVfit.git TauAnalysis/ClassicSVfit -b bbtautau_LegacyRun2
git clone https://github.com/svfit/SVfitTF TauAnalysis/SVfitTF
git clone git@github.com:francescobrivio/StandaloneSVfit.git TauAnalysis/StandaloneSVfit
scram b -j 8
```

### Running instructions
After installation, update the `run_svfit.py` script with the desired input and output file names, and do:
```
python3 run_svfit.py
```
