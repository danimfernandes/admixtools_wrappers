#!/usr/bin/python3

__author__ = 'daniel'

import sys
import os

print("< MERGINGIT - Wrapper to quickly merge two datasets with 'mergeit' >\n")

## Description and Usage ##
helpa = """
    # Description and Usage #
    > 1. Description
    Quickly merge two datasets in EIGENSTRAT or [PACKED]ANCESTRYMAP formats using 'mergeit' from the 'admixtools' package.
    This wrapper script creates the parameter file using default options and merges the two given datasets as arguments.

    > 2. Requirements
    Python modules:
        -os
        -sys

    > 3. Usage
    Input:
    mergingit.py fooDataset barDataset mergedDataset

    Output:
    mergedDataset.geno
    mergedDataset.snp
    mergedDataset.ind

    Example:
    >>> mergingit.py myDataset1 myDataset2 myMergedDataset
    """

cwd = os.getcwd()
    ## Command-line argument and general error checking ##
comLen = len(sys.argv)
if comLen == 1 or comLen == 3:
    print("\t> ERROR: Three command-line arguments are needed. Type '{} -h' for help.")
    quit()
if comLen > 4:
    print("\t> ERROR: Only three command-line arguments are needed. Type '{} -h' for help.")
    quit()
if comLen == 2 and sys.argv[1] == "-h":
    print(helpa)
    quit()
elif comLen == 2:
    print("\t> ERROR: Three command-line arguments are needed. Type '{} -h' for help.")
datasetA=sys.argv[1]
datasetB=sys.argv[2]
mergedDataset=sys.argv[3]

print("\tDataset 1: " + datasetA)
print("\tDataset 2: " + datasetB)
print("\tMerged Dataset: " + mergedDataset + "\n")

fout = open('MERGEIT', 'w')

fout.write("geno1: " + datasetA + ".geno\nsnp1: " + datasetA + ".snp\nind1: " + datasetA + ".ind\ngeno2: " + datasetB + ".geno\nsnp2: " + datasetB + ".snp\nind2: " + datasetB + ".ind\n")
fout.write("genooutfilename: " + mergedDataset + ".geno\nsnpoutfilename: " + mergedDataset + ".snp\nindoutfilename: " + mergedDataset + ".ind\n")

fout.close()

os.system("mergeit -p MERGEIT > /dev/null")