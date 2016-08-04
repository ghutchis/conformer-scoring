#!/usr/bin/env python

import sys, os, math
import numpy as np

for f in sys.argv[1:]:
    with open(f) as fp:
        lastJob = ''
        rmsd = []
        for line in fp:
            items = line.split()
            # Neutral_jobs/omegacsd_KEBVES rmsd12.outRMSD omegacsd_KEBVES 0.374077
            if len(items) < 4:
                print "weirdness with: ", line
                break
            if items[0] != lastJob:
                if len(rmsd) != 0:
                    print lastJob, len(rmsd), np.max(rmsd), np.min(rmsd), np.mean(rmsd), np.std(rmsd)
                rmsd = []
                lastJob = items[0]

            val = float( items[3] )
            if not (math.isnan(val) or math.isinf(val)):
                rmsd.append(float( items[3] ))
        print lastJob, len(rmsd), np.max(rmsd), np.min(rmsd), np.mean(rmsd), np.std(rmsd)
