import pandas as pd

df = pd.read_csv("C:\\Users\\Mahmood Yousaf\\Downloads\\tcga2tile\\camelyon16.csv")
print(df["slide_id"].values)