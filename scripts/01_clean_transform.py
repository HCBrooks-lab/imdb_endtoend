"""
ETL Step 01: Read raw CSV, basic cleaning, save to data_processed.
Run:  python scripts/01_clean_transform.py
"""
import pandas as pd
import numpy as np
# From sqlalchemy import create_engine  
from utils.io_paths import DB_PATH, CSV_PATH, OUTPUT_CLEAN, ensure_dirs
from pathlib import Path

def read_sources() -> pd.DataFrame:
    df_csv = pd.read_csv(CSV_PATH)
    return df_csv

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns] # Normalizing
    for c in df.select_dtypes(include="object").columns: # Trimming
        df[c] = df[c].astype(str).str.strip()
    rename_map = {
        "movie_title": "title",
        "title_year": "year",
        "duration": "runtime_min",
        "imdb_score": "rating",
        "genres": "genres",
        "director_name": "director",
        "gross": "gross_usd",
        "budget": "budget_usd",
    }
    df = df.rename(columns = rename_map)
    key_cols = [c for c in ["title", "year"] if c in df.columns] # Deduplicating
    if key_cols:
        df = df.drop_duplicates(subset=key_cols)
    for c in ["year", "runtime_min", "rating", "gross_usd", "budget_usd"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors = "coerce")
    if "year" in df.columns:
        df["decade"] = (df["year"] // 10 * 10).astype("Int64")
    return df

def main():
    ensure_dirs() # Confirming Directory 

        # --- quick path sanity check ---
    print("CSV_PATH:", CSV_PATH)
    print("CSV exists? ->", CSV_PATH.exists())
    print("Output will be:", OUTPUT_CLEAN)
        # --------------------------------

    df = read_sources()
    df_clean = basic_clean(df)
    df_clean.to_parquet(OUTPUT_CLEAN, index = False)

    csv_mirror = OUTPUT_CLEAN.with_suffix(".csv")
    df_clean.to_csv(csv_mirror, index = False)

    print(f"Saved cleaned dataset to:\n {OUTPUT_CLEAN}\n {csv_mirror}")
    print(f"Rows: {len(df_clean):,} | Columns: {len(df_clean.columns)}")

if __name__ == "__main__":
    main()
