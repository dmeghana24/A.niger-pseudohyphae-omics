
import pandas as pd

df = pd.read_csv("../data/raw/proteomics_results.csv")
df = df[df['Score'] > 20]
df[['ProteinID', 'Sample1', 'Sample2', 'Sample3']].to_csv("../data/processed/proteomics_abundance.csv", index=False)
