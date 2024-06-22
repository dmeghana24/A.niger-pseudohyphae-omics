
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
