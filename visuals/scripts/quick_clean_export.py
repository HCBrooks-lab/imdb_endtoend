import pandas as pd
from pathlib import Path

# Locate project root
ROOT = Path(__file__).resolve().parents[1]

# File paths
raw = ROOT / "data_raw" / "movie_metadata.csv"
outdir = ROOT / "data_processed"
outdir.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(raw)

# Standardize column names
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace(r"[^\w_]+", "", regex=True)
)

# Select useful columns
keep_cols = [c for c in df.columns if c in (
    "movie_title","title_year","genres","imdb_score","duration",
    "color","num_voted_users","gross","budget","director_name",
    "actor_1_name","actor_2_name","actor_3_name","language","country"
)]
if keep_cols: 
    df = df[keep_cols]

# Trim whitespace in text columns
for c in df.select_dtypes(include="object").columns:
    df[c] = df[c].astype(str).str.strip()

# Drop duplicates and rows missing movie title
df = df.drop_duplicates().dropna(subset=["movie_title"])

# Convert to numeric types where appropriate
if "title_year" in df:
    df["title_year"] = pd.to_numeric(df["title_year"], errors="coerce")
if "imdb_score" in df:
    df["imdb_score"] = pd.to_numeric(df["imdb_score"], errors="coerce")

# Output files
csv_path = outdir / "movies_clean.csv"
pq_path  = outdir / "movies_clean.parquet"

df.to_csv(csv_path, index=False)
df.to_parquet(pq_path, index=False)

print(f"✅ Wrote: {csv_path}")
print(f"✅ Wrote: {pq_path}")
print(f"Rows: {len(df):,}  |  Columns: {len(df.columns)}")
