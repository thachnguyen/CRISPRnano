# CRISPNano
CRISPRnano is a javascript-based program that was developed for rapid deep sequencing based genotyping of nuclease edited cell clones. CRISPRnano supports noisy Oxford Nanopore but also Next Generation Sequencing (NGS) reads such as Illumina and PacBio or Sanger Sequencing.
## Input data:

CRISPRnano analyzes FASTQ output files from Illumina or ONT. Our webserver analyzes multiple samples and support up to 96 fastq files. We recommend file's size smaller than 200MB. Make sure that the correct ordering is applied in the file browser. The file allocation to individual pie charts can be verified by the numbers given at alignment track.
Our data contains multiple small FASTQ files, we can concatenate them into a lower number of aggregated samples using command cat under Linux or type under Windows environment.

## Reference sequences
Reference amplicon length should be in the range of 200-300 bases with the nuclease target site located roughly in the middle. You can get the reference from Ensembl database.

## Nuclease Target Site
The Nuclease Target Site sequence has to be in the same orientation as the reference sequence above. The Nuclease Target Site is briefly checked if it is contained in Reference genome

## Interested region and Offset centre
For ONT reads, it is recommended to use -/+15 bases around the predicted DNA lesion. Larger regions are prone to false positive indels. Larger regions (total of 200-250 bp) can be safely used with Illumina reads. You can drag and drop the central point of the predicted double strand break in the genomic sequence to the left or to the right. Default 0 is double strand breaking point.

## Targeting mutagenesis oligonucleotide
Donor oligonucleotide sequence used to introduce a site specific genomic modification. The sequence entered should be in the same orientation as the amplicon sequence.

## Indel Threshold
The Indel Threshold percentage determines at what relative occurrence an individual indel mutation is considered as a unique allele of the respective clone analyzed, and is thus displayed in the alignment list. Low threshold values can result in false positive allele calling due to sequencing errors, whereas high threshold values result in false negative allele calling. Values in between 0 - 100 % can be entered. We recommend to use 5% for ONT reads and 2% for Illumina reads (default is set to 5%).

## Code Availability
The source code for CRISPRnano is available at https://github.com/thachnguyen/CRISPRnano

## Test data
The testdata for CRISPRnano is available at our test sample at https://iufduesseldorf-my.sharepoint.com/:u:/g/personal/thach_nguyen_iuf-duesseldorf_de/ER4kM3RQaRJLiltUCpcT2iMBiEvGvs3u2NiDTdtSPBLE1Q?e=8FEAJc.

## Browser compatibility
|OS Version|Chrome|Firefox|Microsoft Edge|Safari|
|-|-|-|-|-|
|Linux|	Ubuntu 20.04|Version 99.0.4844.51|98.0|n/a|n/a
|-|-|-|-|-|
|MacOS|Monterey|Version 99.0.4844.51|98.0|n/a|15.3
|-|-|-|-|-|
|Windows 10|Version 99.0.4844.51|98.0|99.0.115039|n/a

