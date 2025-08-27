## IMDb End-to-End Data Analysis
This project is an end-to-end data analysis pipeline built using an IMDb movie dataset. It demonstrates the complete workflow of a data analyst from raw data ingestion through transformation, exploratory analysis, and visualization. 

---

## Structure
- data_raw: Original source files (CSV, SQLite)
- data_processed: Cleaned & transformed outputs (Parquet, CSV)
- notebooks: Jupyter notebooks for profiling EDA
- scripts: Python scripts for ETL and processing
- visuals: Saved plots and figures
- requirements.txt: Project dependencies
- READMD.md: Project documentation

---

## Objectives
- Build a reproducible ETL pipeline for raw IMDb data.
- Perform data cleaning/transformation.
- Explore the data through EDA and visualizations.
- Present findings in a way that simulates real-world deliverables.

---

## Current Analysis and Visuals
- Movies Per Decade (with and without labels)
- Movies per Genre (distributed)
- Runtime Distribution (histogram of movie lengths)

---

## Tools and Libraries
- Python: pandas, matplotlib, seaborn
- SQLite: for structured querying
- Jupyter Notebook: EDA and documentation
- VS Code: Development environment

---

## Future Additions
- Expanding analysis to include:
    - Top actors/actresses by number of films.
    - Trends in average movie ratings over time.
    - Relationship between budget, revenue, and IMDb rating.
    - Adding SQL queries directly for data exploration.
    - Integrate a dashboard (Tableau or Power BI) version of visuals.
    - Creating a summary report notebook with insights + storytelling.
 
---

## Key Takeaways (so far)
Clear rise in movie production during the 1990s–2010s.
Ratings distribution is skewed around 6–7, not bell-shaped.
Certain genres dominate the dataset more than others.
