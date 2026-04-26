import pandas as pd

# sample data create pannrom
data = {
    "name": ["ram", "sam", None, "raja"],
    "age": [25, None, 30, 22]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# missing values remove pannrom
df_clean = df.dropna()

print("\nCleaned Data:")
print(df_clean)
