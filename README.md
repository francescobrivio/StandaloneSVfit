## StandaloneSVfit
SVfit implementation for running on ROOT DataFrames.

### Download instructions
```
cmsrel CMSSW_13_0_10
cd CMSSW_13_0_10/src
cmsenv
git clone https://github.com/LLRCMS/ClassicSVfit.git TauAnalysis/ClassicSVfit -b bbtautau_LegacyRun2
git clone https://github.com/svfit/SVfitTF TauAnalysis/SVfitTF
git clone https://github.com/francescobrivio/StandaloneSVfit.git TauAnalysis/StandaloneSVfit
scram b -j 8
```

### Running instructions
After installation:
```
cd TauAnalysis/StandaloneSVfit
```
and run with:
```
python3 run_svfit.py \
  -i /path/to/input/file.root \
  -o /path/to/output/file.root \
  -n nMax \
  -r reduced
```
where `-n` and -`r` are mostly for debugging purposes (you can omit them for production):
- `nMax` is the maximum number of events to filter the RDF
- `reduced` is a bool to store only the svfit columns in the otput RDF
