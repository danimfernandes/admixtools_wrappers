#!/usr/bin/python3

__author__ = 'daniel'

import sys
import os

print("< F4SINGLETEST - Quickly run a single f4-statistic test from the terminal >\n")

## Description and Usage ##
helpa = """
    # Description and Usage #
    > 1. Description
    Quickly runs qpDstat to calculate a single f4-statistic from the terminal.
    This wrapper script creates the parameter file using default options.

    > 2. Requirements
    Python modules:
        -os
        -sys

    > 3. Usage
    Input:
    f4singleTest.py fooDataset popW popX popY popZ

    Output:
    f4out_popW_popX_popY_popZ

    Example:
    >>> f4singleTest.py myDataset1 Mbuti.DG Anatolia_N Iran_N Levant_N
    """

cwd = os.getcwd()
    ## Command-line argument and general error checking ##
comLen = len(sys.argv)
if comLen == 2 and sys.argv[1] == "-h":
    print(helpa)
    quit()
if comLen == 1 or comLen == 2 or comLen == 3 or comLen == 4 or comLen == 5:
    print("\t> ERROR: Five command-line arguments are needed. Type 'f4singleTest.py -h' for help.")
    quit()
if comLen > 6:
    print("\t> ERROR: Only five command-line arguments are needed. Type 'f4singleTest.py -h' for help.")
    quit()

datasetIn=sys.argv[1]
popW=sys.argv[2]
popX=sys.argv[3]
popY=sys.argv[4]
popZ=sys.argv[5]

print("\tDataset: " + datasetIn)
print("\tPop W: " + popW)
print("\tPop X: " + popX)
print("\tPop Y: " + popY)
print("\tPop Z: " + popZ)


fout = open('f4_param_Temp', 'w')
fout.write("genotypename: " + datasetIn + ".geno\nsnpname: " + datasetIn + ".snp\nindivname: " + datasetIn + ".ind\npopfilename: f4_pop_Temp\nf4mode: YES\ndetails: YES\nprintsd: YES")
fout.close()

fout1 = open("f4_pop_Temp", "w")
fout1.write(popW + " " + popX + " " + popY + " " + popZ)
fout1.close()

os.system("qpDstat -p f4_param_Temp > f4out_" + popW + "_" + popX + "_" + popY + "_" + popZ)
