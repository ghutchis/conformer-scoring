import sys
import pandas as pd
import numpy as np
from scipy.stats import linregress

# To run this file:
# Argument 1: Text file containing data Argument 2: File containing additional DFT calculations

def count_1(x):
    plus_1 = min(x) + 1
    value = [i for i in x if i <= plus_1]
    return len(value)

def count_2(x):
    plus_2 = min(x) + 2
    value = [i for i in x if i <= plus_2]
    return len(value)

def count_3(x):
    plus_3 = min(x) + 3
    value = [i for i in x if i <= plus_3]
    return len(value)

def count_4(x):
    plus_4 = min(x) + 4
    value = [i for i in x if i <= plus_4]
    return len(value)

def count_5(x):
    plus_5 = min(x) + 5
    value = [i for i in x if i <= plus_5]
    return len(value)

def count_6(x):
    plus_6 = min(x) + 6
    value = [i for i in x if i <= plus_6]
    return len(value)

def count_7(x):
    plus_7 = min(x) + 7
    value = [i for i in x if i <= plus_7]
    return len(value)

def count_8(x):
    plus_8 = min(x) + 8
    value = [i for i in x if i <= plus_8]
    return len(value)

def count_9(x):
    plus_9 = min(x) + 9
    value = [i for i in x if i <= plus_9]
    return len(value)

def count_10(x):
    plus_10 = min(x) + 10
    value = [i for i in x if i <= plus_10]
    return len(value)

# Make sure there are headers on the column named mol entry MMFF94 PM7 DFT
dataFile = sys.argv[1]
newData = sys.argv[2]
df_a = pd.read_csv(dataFile, sep=" ", header=0)
df_a['mol_entry'] = df_a['mol'].map(str) + df_a['entry']
df_b = pd.read_csv(newData, sep=",", header=0)
df_b['mol_entry'] = df_b['mol'].map(str) + df_b['entry']
df = pd.merge(df_a, df_b, how='left', on='mol_entry')

df_DFT = df
del df_DFT['mol_y']
del df_DFT['entry_y']

both_populated = df_DFT[['DFT', 'oldDFT']].notnull().all(axis=1)
one_populated = df_DFT[['DFT', 'oldDFT']].isnull().any(axis=1)

df_DFT.loc[both_populated, 'DFT_full'] = df_DFT.loc[both_populated, 'DFT']
df_DFT.loc[one_populated, 'DFT_full'] = np.nansum([np.asarray(df_DFT.loc[one_populated, 'DFT']), np.asarray(df_DFT.loc[one_populated, 'oldDFT'])], axis=0)
df_DFT = df_DFT[(df_DFT.DFT_full != 0)]
df_DFT = df_DFT[np.isfinite(df_DFT['DFT_full'])]
#Convert DFT energies from Hartree to kcal
df['DFT_full'] = df['DFT_full']*627.503

df['mmff94_pm7'] = zip(df.MMFF94, df.PM7)
df_DFT['MMFF94_dft'] = zip(df_DFT.MMFF94, df_DFT.DFT_full)
df_DFT['pm7_dft'] = zip(df_DFT.PM7, df_DFT.DFT_full)

df2 = pd.concat([df.mol_x, df.MMFF94], axis=1, keys=['mol_x', 'MMFF94'])
df3 = pd.concat([df.mol_x, df.PM7], axis=1, keys=['mol_x', 'PM7'])
df4 = pd.concat([df_DFT.mol_x, df_DFT.DFT_full], axis=1, keys=['mol_x', 'DFT_full'])

Count_MMFF94 = df2.groupby('mol_x').MMFF94.agg([count_1, count_2,count_3, count_4,count_5,count_6,count_7,count_8,count_9,count_10, len])
Count_PM7 = df3.groupby('mol_x').PM7.agg([count_1, count_2,count_3, count_4,count_5,count_6,count_7,count_8,count_9,count_10, len])
Count_DFT = df4.groupby('mol_x').DFT_full.agg([count_1, count_2,count_3, count_4,count_5,count_6,count_7,count_8,count_9,count_10, len])

Count_MMFF94.to_csv('Count_MMFF94.txt')
Count_PM7.to_csv('Count_PM7.txt')
Count_DFT.to_csv('Count_DFT.txt')

print Count_MMFF94
print Count_PM7
print Count_DFT
