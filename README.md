# 🦠 A.niger-pseudohyphae-omics

**A reproducible multi-omics pipeline for dissecting pseudohyphal growth in *Aspergillus niger***

---

## 🌟 Overview

This repository provides an end-to-end workflow for integrating transcriptomic and proteomic data to investigate the genetic and molecular mechanisms underlying pseudohyphal growth in *Aspergillus niger*. The pipeline includes data preprocessing, differential analysis, pathway/network integration, and results visualization.

---

## 🧬 Motivation

Pseudohyphal growth in *A. niger* is a critical adaptive response relevant to fungal biology and biotechnology. By integrating RNA-seq and proteomics data, we can uncover regulatory pathways and key drivers of filamentous development.

---

## 🛠️ Pipeline Workflow

<!--

```mermaid
graph TD
    A[Raw RNA-seq Data] --> B[QC & Alignment]
    B --> C[Differential Expression (DESeq2)]
    C --> D1[Functional Enrichment]
    A2[Raw Proteomics Data] --> B2[Quantification & QC]
    B2 --> C2[Differential Abundance]
    C2 --> D2[Protein Network Analysis]
    C --> E[Integration with Proteomics]
    C2 --> E
    E --> F[Pathway & Network Visualization]

# Aspergillus niger Pseudohyphal Growth Omics Pipeline

A modular, reproducible pipeline for mapping genes and proteins involved in pseudohyphal growth in *Aspergillus niger*, integrating RNA-seq, proteomics, and functional annotation.


## Testing, QC & Example Results

- See `/notebooks/qc_rnaseq_demo.ipynb` for RNA-seq QC (library size, PCA, batch).
- See `/notebooks/example_pipeline_run.ipynb` for a complete mock run (differential expression, volcano plot).
- Example input data: `/test_data/`
- Example output: `/results/mock_DEGs.csv`, `/figures/volcano_plot_mock.png`, `/figures/qc_library_size.png`, etc.

**How to run:**  
```bash
conda env create -f environment.yml
jupyter notebook
# open and run the notebooks in /notebooks/
```

Testing, QC & Example Results
This repository now contains documented quality control, example pipeline runs, and outputs with clear provenance—see commit history for exact timestamps.

2024-06-18: Added mock RNA-seq count and metadata files for pipeline testing (`/test_data/mock_counts.csv`, `/test_data/mock_metadata.csv`).

2024-06-19: Added RNA-seq QC notebook and figures for library size and PCA using mock data (`/notebooks/qc_rnaseq_demo.ipynb`, `/figures/qc_library_size.png`, `/figures/qc_pca_mock.png`).

2024-06-19: Visualized batch effects in PCA plot in RNA-seq QC notebook (`/figures/qc_batch_effect_mock.png`).

2024-06-19: Added a full example pipeline notebook from counts to candidate genes, with volcano plot and outputs (`/notebooks/example_pipeline_run.ipynb`, `/figures/volcano_plot_mock.png`).

2024-06-20: Added example result tables and output plots, including mock differential gene tables.

2024-06-22: Updated this README with current documentation and workflow summary.

What’s Included
`/test_data/`: Minimal test data to demonstrate workflow integrity.

`/notebooks/qc_rnaseq_demo.ipynb`: Quality control, library size checks, PCA, and batch effect visualization.

`/notebooks/example_pipeline_run.ipynb`: End-to-end mock pipeline from raw counts to candidate gene discovery and differential analysis.

`/figures/`: All output plots (library QC, PCA, batch, volcano).

`/results/`: Example output tables for downstream interpretation.

How to run:
```bash
Install dependencies:

conda env create -f environment.yml
conda activate a_niger_env
jupyter notebook
#Open any notebook in /notebooks/ and follow the cells for fully reproducible testing and analysis using provided mock data.
```


