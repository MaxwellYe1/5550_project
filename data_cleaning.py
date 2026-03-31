import pandas as pd
import numpy as np

data_path = "climate_data.csv"

df = pd.read_csv(data_path)

print("Original shape:", df.shape)
print("Original columns:", df.columns.tolist())

# Standardize column names
df.columns = df.columns.str.strip().str.upper()

keep_cols = [
    "STATION", "DATE", "PRCP", "SNOW", "SNWD",
    "TMAX", "TMIN", "TOBS",
    "WT01", "WT03", "WT04", "WT05", "WT06", "WT11"
]

existing_cols = [col for col in keep_cols if col in df.columns]
print("Existing kept columns:", existing_cols)

df = df[existing_cols].copy()
print("After column selection:", df.shape)

# Parse date and sort
print("Raw DATE examples:", df["DATE"].head(10).tolist())

df["DATE"] = df["DATE"].astype(str).str.strip().str.replace('"', '', regex=False)
df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

print("Missing DATE after parsing:", df["DATE"].isna().sum())

df = df.dropna(subset=["DATE"]).sort_values("DATE").reset_index(drop=True)
print("After DATE cleaning:", df.shape)

# Convert numeric columns
numeric_cols = ["PRCP", "SNOW", "SNWD", "TMAX", "TMIN", "TOBS"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print("Missing TMAX:", df["TMAX"].isna().sum())
print("Missing TMIN:", df["TMIN"].isna().sum())

# Convert weather indicator columns to binary
wt_cols = [col for col in ["WT01", "WT03", "WT04", "WT05", "WT06", "WT11"] if col in df.columns]
for col in wt_cols:
    df[col] = np.where(df[col].notna(), 1, 0)

# Fill precipitation/snow related missing values with 0
for col in ["PRCP", "SNOW", "SNWD"]:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# Keep rows where core temperature variables exist
df = df.dropna(subset=["TMAX", "TMIN"]).reset_index(drop=True)
print("After TMAX/TMIN cleaning:", df.shape)

# Basic calendar features
df["YEAR"] = df["DATE"].dt.year
df["MONTH"] = df["DATE"].dt.month
df["DAYOFYEAR"] = df["DATE"].dt.dayofyear

df.to_csv("cleaned_climate_data.csv", index=False)
print("Cleaned file saved.")