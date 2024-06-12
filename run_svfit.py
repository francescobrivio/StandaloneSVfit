# Imports
import os
import sys ; assert sys.hexversion>=((3<<24)|(7<<16)), 'Python 3.7 or greater required' # a binary joke is worth 111 words
sys.path.append(os.getcwd())
import ROOT

# Import StandaloneSVfit class
ROOT.gROOT.ProcessLine('.L /gwpool/users/brivio/CCLUB/transformerTT/CMSSW_13_0_10/src/TauAnalysis/StandaloneSVfit/interface/StandaloneSVfit.h')

# Define string to run SVfit
svfit_string = '''
auto svfit = StandaloneSVfit();

int verbosity    = 0;
int pairType     = 0;
int DM1          = -1;
int DM2          = 1;
double tau1_pt   = 42.122390;
double tau1_eta  = -0.149487;
double tau1_phi  = 0.1000680;
double tau1_mass = 0.10874185;
double tau2_pt   = 111.85233;
double tau2_eta  = -0.499875;
double tau2_phi  = 1.218472;
double tau2_mass = 1.1941469;
double met_pt    = 46.620235;
double met_phi   = 5.5289621;
double met_covXX = 834.84625;
double met_covXY = 234.44636;
double met_covYY = 915.31604;

auto result = svfit.FitAndGetResultWithInputs(verbosity, pairType, DM1, DM2, tau1_pt, tau1_eta, tau1_phi, tau1_mass, tau2_pt, tau2_eta, tau2_phi, tau2_mass, met_pt, met_phi, met_covXX, met_covXY, met_covYY);
return result;
'''

# Input file
infile = '/gwdata/users/brivio/SVFit_standalone/original_files/ggH_nanoHTT_2.root' # DY_nanoHTT_2.root
print('- Reading File:', infile)

# Open RDF
df = ROOT.RDataFrame('Events', infile)
all_events = df.Count().GetValue()
print('- Original entries:', all_events)

# Select only 2 entries
df = df.Range(2)
ranged_events = df.Count().GetValue()
print('- Ranged entries:', ranged_events)

# Run SVfit
df = df.Define('svfit_m', svfit_string)
print('Defined svfit_m column')

# Save snapshot
print('Start snapshot')
df.Snapshot('outputTree', 'outputFile.root', {'run', 'luminosityBlock', 'event', 'svfit_m'})
print('Done snapshot')

#import pdb; pdb.set_trace()

'''
cols = ('run', 'luminosityBlock', 'event', 'svfit_m')
d2 = df.Display(cols)
print(d2.AsString())
'''


