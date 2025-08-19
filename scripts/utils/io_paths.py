from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

def find_project_root() -> Path:
    """Walk upward until we find the folder that has requirements.txt."""
    p = Path(__file__).resolve()
    for parent in [p] + list(p.parents):
        if (parent / "requirements.txt").exists():
            return parent
    # Fallback (old assumption)
    return Path(__file__).resolve().parents[2]

PROJECT_ROOT = find_project_root()

DB_PATH = PROJECT_ROOT / os.getenv("DB_PATH", "data_raw/imdb_movies.db")
CSV_PATH = PROJECT_ROOT / os.getenv("CSV_PATH", "data_raw/movie_metadata.csv")
OUTPUT_CLEAN = PROJECT_ROOT / os.getenv("OUTPUT_CLEAN", "data_processed/movies_clean.parquet")

def ensure_dirs():
    (PROJECT_ROOT / "data_processed").mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "visuals").mkdir(parents=True, exist_ok=True)