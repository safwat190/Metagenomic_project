# Metagenomic_project
Analysis of the 16S sequencing data of 133 fecal samples  for the metagenomics course project.

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
### R scripts: Using Rhea in R
#### Normalization.R
The total number of raw read counts for each sample were normalized to a fixed total which represents the minimum read raw counts among the samples: 957.
#### Alpha-Diversity.R
Alpha diversity was calculated for each sample of normalized data to allow direct comparisons among the 133 samples in the study.
#### Beta-Diversity.R
To measure the similarity between different microbial profiles described by the identified 395 OTUs, beta diversity calculations were performed.
#### Taxonomic-Binning.R
To estimate the taxonomic composition of samples, the taxonomic classification of the 395 OTUs was performed.
#### Serial-Group-Comparisons.R
To detect the difference in composition and abundances of the samples, the samples were classified based on the original metadata file into inactive, baseline and active (based on the disease status). ANOVA was performed using the non-parametric test Kruskal-Wallis Rank Sum to obtain the pairwise test significance values which in turn was corrected using the Benjamini-Hochberg method. For a taxonomy to be considered for the statistical testing:
#### - It has to have a minimum relative abundance < 0.5. Variables with < 0.5 relative abundance were replaced by zero.
#### - It has to be present in at least 30% of samples of either group.
#### - It has to have a relative abundance median of at least 1% across all groups.

### R script: Using Seurat
Seurat package in R was used to perform differential analysis as follows.......
### load packages
```
library(Seurat)
library(dplyr)
library(Matrix)
library(ggplot2)
```

### Read taxonomic relative abundance and metadata
```
metadata = read.csv('/Seurat_meta.csv',row.names = 1,header = T, sep = '\t')
counts = read.csv('/Seurat_counts.csv',row.names = 1,header = T, sep = '\t')
```

### Create a Seurat object
```
object = CreateSeuratObject(counts = counts, meta.data = metadata)
```

### Log Normalize Counts
```
object = NormalizeData(object, normalization.method = "LogNormalize")
```

### Identify differentially expressed taxonomic groups among inactive, baseline and active groups
```
Idents(object) = 'disease_state'
group_markers = FindAllMarkers(object, logfc.threshold = 0, min.pct = 0.2)
write.csv(group_markers, '/Group markers.csv')
```

### Identify differentially expressed taxonomic groups between active and inactive status
```
active_vs_inactive = FindMarkers(object, ident.1 = 'Active', ident.2 = 'Inactive', logfc.threshold = 0, min.pct = 0.2)
write.csv(active_vs_inactive, '/active_vs_inactive.csv')
```

### Generating heatmap and dotplots: First define the list of taxonomies and then plot.
```
object = ScaleData(object, features = rownames(object))
DoHeatmap(object, features = Taxons_of_interest)
DotPlot(object, features = Taxons_of_interest2)+theme(axis.text.x = element_text(angle = 45, hjust=1))
```
### End of analysis.
