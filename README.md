# conformer-scoring

Supporting data and scripts relevant to an evaluation of force field
and quantum methods for conformer scoring via energy ranking.

Connected to the manuscript

"A Sobering Assessment of Small-Molecule Force Field Methods for Low Energy Conformer Predictions"
arXiv: https://arxiv.org/abs/1705.04308

## Brief description of files:

Jupyter / ipython notebooks for converting CSV data for analysis:
* MMAnalysis.ipynb
* OptAnalysis.ipynb

Output files and geometries:
* atoms.tar.bz2 - compiled ORCA output files for computing atomization energies
* conformers.tar.bz2 - compiled optimized geometries with MMFF94, PM7,
  and DFT

Compiled data:
* data.csv - energies corresponding to
data-merge.csv
mm-data.csv

Scripts:
* compile-conformers.py - read output files, compile conformer
geometries and data.csv file
* consolidate-data.py - convert data.csv file into data-merge.csv file

Analysis CSV files created by OptAnalysis jupyter notebook:
* dft@mmff_dft@dft_stats.csv
* dft@mmff_dft@pm7_stats.csv
* dft@pm7_dft@dft_stats.csv
* mmff@mmff_dft@dft_stats.csv
* mmff@mmff_dft@pm7_stats.csv
* mmff@pm7_dft@dft_stats.csv
* pm7@dft_dft@dft_stats.csv
* pm7@dft_pm7@pm7_stats.csv
* pm7@mmff_pm7_stats.csv
* pm7@pm7_dft@dft_stats.csv
* pm7@pm7_dft@pm7_stats.csv

Analysis CSV files for MM vs. PM7 comparisons created by MMAnalysis
jupyter notebook:

* mmff_pm7_stats.csv
* gaff_pm7_stats.csv
* uff_pm7_stats.csv

Auxillary scripts:

* rmsd.py - analyze the heavy-atom root mean square displacement
  (RMSD) using Open Babel
