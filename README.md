# Metagenomic_project
Analysis of 16S RNA sequencing for 133 samples for the metagenomics course project.

## Samples were retrieved from the NCBI database (accession SRA: PRJNA565903)
https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA565903

### R script to download the samples
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
