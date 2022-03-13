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
### Command line: Run a perl script to merge samples to be compatible with IMNGS software
The perl script is available in the folder "Scripts"
```
perl remultiplexor-paired.pl
```
