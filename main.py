import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('business-licences.csv', delimiter=';')

print("Business Licenses Dataset")
print("=" * 50)
print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nColumn names:\n{df.columns.tolist()}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
