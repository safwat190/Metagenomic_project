# Metagenomic_project
Analysis of 16S RNA sequencing for 133 samples for the metagenomics course project.

#### Samples and their URLs were retrieved from the NCBI database (accession SRA: PRJNA565903)
https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA565903

### R script: Download the samples using their URLs
```
library(downloader)
options(timeout=100000)
for(url in download.links)
{
    filename = gsub(".*\\/(.*)\\..*", "\\1", url)
    download(url, destfile=filename)
}
setwd("~/Downloads/0_metagenome_project")
download.links = SraRunInfo$download_path
```
### Command line: Split the SRA files into 133 samples (266 files representing 133 pairs of forward and reverse reads)
```
fastq-dump --split-files *
```
### Command line: Quality check and merging the resulting 266 quality reports
```
fastqc *.fastq
multiqc . --interactive
```
## Command line: Run a perl script to merge samples to be compatible with IMNGS software
The perl script is available in the folder "Scripts"
```
perl remultiplexor-paired.pl
```
## R script: Using Rhea in R
### Normalization.R
The total number of raw read counts for each sample were normalized to a fixed total which represents the minimum read raw counts among the samples: 957.
### Alpha-Diversity.R
Alpha diversity was calculated for each sample of normalized data to allow direct comparisons among the 133 samples in the study.
### Beta-Diversity.R
To measure the similarity between different microbial profiles described by the identified 395 OTUs, beta diversity calculations were performed.
### Taxonomic-Binning.R
To estimate the taxonomic composition of samples, the taxonomic classification of the 395 OTUs was performed.
### Serial-Group-Comparisons.R
To detect the difference in composition and abundances of the samples, the samples were classified based on the original metadata file into inactive, baseline and active (based on the disease status). ANOVA was performed using the non-parametric test Kruskal-Wallis Rank Sum to obtain the pairwise test significance values which in turn was corrected using the Benjamini-Hochberg method. For a taxonomy to be considered for the statistical testing:
#### - It has to have a minimum relative abundance < 0.5. Variables with < 0.5 relative abundance were replaced by zero.
#### - It has to be present in at least 30% of samples of either group.
#### - It has to have a relative abundance median of at least 1% across all groups.
### - Over-Time-Serial-Comparisons.R
Not yet
### Correlations.R
Not yet

## R script: Using Seurat
Seurat package in R was used to perform differential analysis as follows.......
```
Code here
```
