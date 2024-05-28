import pandas as pd 
df = pd.read_csv("exists.csv")
# print(df['PATIENT'])
if "TCGA-AG-3594-01Z-00-DX1.83a27a62-0ddd-48e0-ba34-1ba6d8aa9526" in df['PATIENT'].values:
    print("Exist")
    