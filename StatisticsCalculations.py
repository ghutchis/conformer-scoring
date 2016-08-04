import sys
import pandas as pd
import numpy as np
from scipy.stats import linregress
from pandas.stats.api import ols

# To run this file:
# Argument 1: Text file containing data

# Calculates r-squared
def ols_rsq(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1]})
    return pd.ols(x=d.x, y=d.y).r2_adj

# Calculates x-coefficient
def ols_coeff_x(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1]})
    return pd.ols(x=d.x, y=d.y).beta[0]

# Calculates intercept
def ols_coeff_intercept(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1]})
    return pd.ols(x=d.x, y=d.y).beta[1]

# Calculates slope
def linregress_slope(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1]})
    return (linregress(d.x, d.y)[0])

# Calculates spearman correlations
def agg_spearman_corr(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1]})
    return d.corr(method='spearman').values[0, 1]

def multi_var_MMFF_coeff(x):
    l = zip(*x)
    d = pd.DataFrame({'MMFF94': l[0], 'PM7': l[1], 'DFT': l[2]})
    res = pd.ols(y=d['DFT'], x=d[['MMFF94','PM7']])
    return res.beta[0]
    #return pd.ols(y=d.z, x=[[d.x, d.y]]).summary_as_matrix

def multi_var_PM7_coeff(x):
    l = zip(*x)
    d = pd.DataFrame({'MMFF94': l[0], 'PM7': l[1], 'DFT': l[2]})
    res = pd.ols(y=d['DFT'], x=d[['MMFF94','PM7']])
    return res.beta[1]

def multi_var_intercept(x):
    l = zip(*x)
    d = pd.DataFrame({'MMFF94': l[0], 'PM7': l[1], 'DFT': l[2]})
    res = pd.ols(y=d['DFT'], x=d[['MMFF94','PM7']])
    return res.beta[2]

def multi_var_stderr_MMFF(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).std_err[0]

def multi_var_stderr_PM7(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).std_err[1]

def multi_var_stderr_int(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).std_err[2]

def multi_var_pval_MMFF(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).p_value[0]

def multi_var_pval_PM7(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).p_value[1]

def multi_var_pval_int(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).p_value[2]

def multi_var_rsqd(x):
    l = zip(*x)
    d = pd.DataFrame({'x': l[0], 'y': l[1], 'z': l[2]})
    return pd.ols(y=d['z'], x=d[['x','y']]).r2_adj

# Read in data file. Make sure there are titles name,conf,mmffE,mopacE,mmffAtMOPACE,mopacAtMMFFE,uffE,gaffE,orcaE,orcaAtMME, etc.
dataFile = sys.argv[1]
#newData = sys.argv[2]
df = pd.read_csv(dataFile, sep=",", header=0)
#df['name_conf'] = df['name'].map(str) + df['conf']
#df_b = pd.read_csv(newData, sep=",", header=0)
#df_b['mol_entry'] = df_b['mol'].map(str) + df_b['entry']
#df = pd.merge(df_a, df_b, how='left', on='mol_entry')
df['orcaE'] = pd.to_numeric(df['orcaE'], errors='coerce')
df['orcaAtMME'] = pd.to_numeric(df['orcaAtMME'], errors='coerce')

df_DFT = df.copy()
df_DFTAtMME = df.copy()
#del df_DFT['mol_y']
#del df_DFT['entry_y']

#both_populated = df_DFT[['DFT', 'oldDFT']].notnull().all(axis=1)
#one_populated = df_DFT[['DFT', 'oldDFT']].isnull().any(axis=1)

#df_DFT.loc[both_populated, 'DFT_full'] = df_DFT.loc[both_populated, 'DFT']
#df_DFT.loc[one_populated, 'DFT_full'] = np.nansum([np.asarray(df_DFT.loc[one_populated, 'DFT']), np.asarray(df_DFT.loc[one_populated, 'oldDFT'])], axis=0)
#df_DFT = df_DFT[(df_DFT.DFT_full != 0)]

df_DFT = df_DFT[np.isfinite(df_DFT['orcaE'])]
df_DFTAtMME = df_DFT[np.isfinite(df_DFT['orcaAtMME'])]

df['mmffE_mopacE'] = zip(df.mmffE, df.mopacE)
df['gaffE_mopacE'] = zip(df.gaffE, df.mopacE)
df['uffE_mopacE'] = zip(df.uffE, df.mopacE)
df['mopacAtMMFFE_mopacE'] = zip(df.mopacAtMMFFE, df.mopacE)

df_DFT['mmffE_orcaE'] = zip(df_DFT.mmffE, df_DFT.orcaE)
df_DFT['mopacE_orcaE'] = zip(df_DFT.mopacE, df_DFT.orcaE)
df_DFT['all_energies'] = zip(df_DFT.mmffE, df_DFT.mopacE, df_DFT.orcaE)
df_DFT['mmffAtMOPACE_orcaE'] = zip(df_DFT.mmffAtMOPACE, df_DFT.orcaE)
df_DFTAtMME['orcaAtMME_orcaE'] = zip(df_DFTAtMME.orcaAtMME, df_DFTAtMME.orcaE)
df_DFT['mopacAtMMFFE_orcaE'] = zip(df_DFT.mopacAtMMFFE, df_DFT.orcaE)

df2 = pd.concat([df.name, df.mmffE_mopacE], axis=1, keys=['name', 'mmffE_mopacE'])
df3 = pd.concat([df.name, df.gaffE_mopacE], axis=1, keys=['name', 'gaffE_mopacE'])
df4 = pd.concat([df.name, df.uffE_mopacE], axis=1, keys=['name', 'uffE_mopacE'])
df5 = pd.concat([df_DFT.name, df_DFT.mmffE_orcaE], axis=1, keys=['name', 'mmffE_orcaE'])
df6 = pd.concat([df_DFT.name, df_DFT.mopacE_orcaE], axis=1, keys=['name', 'mopacE_orcaE'])
df7 = pd.concat([df_DFT.name, df_DFT.mmffAtMOPACE_orcaE], axis=1, keys=['name', 'mmffAtMOPACE_orcaE'])
df8 = pd.concat([df_DFTAtMME.name, df_DFTAtMME.orcaAtMME_orcaE], axis=1, keys=['name', 'orcaAtMME_orcaE'])
df9 = pd.concat([df_DFT.name, df_DFT.mopacAtMMFFE_orcaE], axis=1, keys=['name', 'mopacAtMMFFE_orcaE'])
df10 = pd.concat([df.name, df.mopacAtMMFFE_mopacE], axis=1, keys=['name', 'mopacAtMMFFE_mopacE'])
df11 = pd.concat([df_DFT.name, df_DFT.all_energies], axis=1, keys=['name', 'all_energies'])

o1 = df2.groupby('name')[['mmffE_mopacE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o2 = df3.groupby('name')[['gaffE_mopacE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o3 = df4.groupby('name')[['uffE_mopacE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o4 = df5.groupby('name')[['mmffE_orcaE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o5 = df6.groupby('name')[['mopacE_orcaE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o6 = df7.groupby('name')[['mmffAtMOPACE_orcaE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o7 = df8.groupby('name')[['orcaAtMME_orcaE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o8 = df9.groupby('name')[['mopacAtMMFFE_orcaE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
o9 = df10.groupby('name')[['mopacAtMMFFE_mopacE']].agg([len, ols_coeff_x, ols_coeff_intercept, ols_rsq, agg_spearman_corr, linregress_slope])
# For multivariate fit use data frame with 'all energies'
#o10 = df11.groupby('name')[['all_energies']].agg([multi_var_MMFF_coeff, multi_var_PM7_coeff, multi_var_intercept, multi_var_stderr_MMFF, multi_var_stderr_PM7, multi_var_stderr_int, multi_var_pval_MMFF, multi_var_pval_PM7, multi_var_pval_int, multi_var_rsqd])

o1.to_csv('mmff94_pm7_stats.txt')
o2.to_csv('gaff_pm7_stats.txt')
o3.to_csv('uff_pm7_stats.txt')
o4.to_csv('mmff_DFT_stats.txt')
o5.to_csv('pm7_DFT_stats.txt')
o6.to_csv('mmffAtpm7_DFT.txt')
o7.to_csv('DFTAtMMFF_DFT.txt')
o8.to_csv('PM7AtMMFF_DFT.txt')
o9.to_csv('PM7AtMMFF_PM7.txt')
o10.to_csv('multivariate_fit.txt')
