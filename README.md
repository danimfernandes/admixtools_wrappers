# A set of wrappers for frequent ADMIXTOOLS operations

**F4SINGLETEST - Quickly run a single f4-statistic test from the terminal**

### 1. Description

Quickly runs qpDstat to calculate a single f4-statistic from the terminal.
This wrapper script creates the parameter file using default options.

### 2. Requirements

Python modules:

-os

-sys

### 3. Usage

Input:

    f4singleTest.py fooDataset popW popX popY popZ

Output:

f4out_popW_popX_popY_popZ

Example:

    f4singleTest.py myDataset1 Mbuti.DG Anatolia_N Iran_N Levant_N

***

**CONVERTINGIT - Wrapper to quickly convert a dataset with 'convertf'**

### 1. Description

Quickly convert a dataset to a desired format accepted by 'convertf' from the 'admixtools' package.
This wrapper script creates the parameter file using default options and uses the 'outputformat' given as an argument.

### 2. Requirements

Python modules:

-os

-sys

Other provided scripts with system wide availability:

- famfile_correction.py

- indfile_correction.py

### 3. Usage

Input:

    convertingit.py fooDataset inputFormat outputFormat

Output:

fooDatasetReduced.geno/bed

fooDatasetReduced.snp/bim

fooDatasetReduced.ind/fam

Example:

    convertingit.py myDataset1 PACKEDPED EIGENSTRAT

***

**MERGINGIT - Wrapper to quickly merge two datasets with 'mergeit'**

### 1. Description

Quickly merge two datasets in EIGENSTRAT or [PACKED]ANCESTRYMAP formats using 'mergeit' from the 'admixtools' package.
This wrapper script creates the parameter file using default options and merges the two given datasets as arguments.

### 2. Requirements

Python modules:

-os

-sys

### 3. Usage

Input:

    mergingit.py fooDataset barDataset mergedDataset

Output:

mergedDataset.geno

mergedDataset.snp

mergedDataset.ind

Example:

    mergingit.py myDataset1 myDataset2 myMergedDataset

***

**REDUCINGIT - Wrapper to quickly reduce a dataset with 'convertf'**

### 1. Description

Quickly reduce a dataset in EIGENSTRAT or [PACKED]ANCESTRYMAP formats using 'convertf' from the 'admixtools' package given a list of populations to keep.
This wrapper script creates the parameter file using default options and uses the 'poplistname' given as an argument.

### 2. Requirements

Python modules:

-os

-sys

### 3. Usage

Input:

    reducingit.py fooDataset poplistnameFile fooDatasetReduced

Output:

fooDatasetReduced.geno

fooDatasetReduced.snp

fooDatasetReduced.ind

Example:

    reducingit.py myDataset1 keep_myPopList myDataset1_reduced
***
