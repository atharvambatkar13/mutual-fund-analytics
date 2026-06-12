import os
import pandas as pd

for file in os.listdir("data/raw"):
    if file.endswith(".csv"):

        path = os.path.join("data/raw", file)

        print("\n" + "=" * 80)
        print(f"FILE: {file}")

        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nFirst 5 Rows:")
        print(df.head())