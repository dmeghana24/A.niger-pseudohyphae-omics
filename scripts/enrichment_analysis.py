
from gprofiler import GProfiler
import pandas as pd

df = pd.read_csv("../results/DEGs.csv")
gp = GProfiler(return_dataframe=True)
res = gp.profile(organism='anidulans', query=list(df['row.names']))
res.to_csv("../results/go_enrichment.csv", index=False)
