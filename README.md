## IMDb End-to-End Data Analysis
An end-to-end analysis of IMDb movie data, combining SQL, Python and visualization to uncover trends in ratings, genres, budgets, and box office performance. 

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
- Top Actors by Film Count (horizontal of movie lengths)
- Ratings by Year (average IMDb ratings over time)
- Budget vs. Revenue by Year (line chart comparison)
- Correlation Analysis (budget, revenue, IMDb rating)
- Directors - Quality & Quantity (ratings vs. film counts)

---

## Tools and Libraries
- Python: pandas, matplotlib, seaborn
- SQLite: for structured querying
- Jupyter Notebook: EDA and documentation
- VS Code: Development environment

---

## Future Additions
- Expanding analysis to include:
    - Adding additional SQL queries to expand exploratory analysis.
    - Developing decade-level visualizations (e.g, average ratings, budget,
      revenue).
    - Incorporate KPI-style dashboards in Tableau/Power BI for interactive
      exploration.
    - Perform deeper storytelling analysis around trends (e.g., genre
      evolution, box office success drivers).
    - Refine README with visuals, insights, and project flow for hiring
      managers. 
    - Top actors/actresses by number of films - completed. 
    - Trends in average movie ratings over time - completed. 
    - Relationship between budget, revenue, and IMDb rating - completed. 
    - Adding SQL queries directly for data exploration - in progress. 
    - Integrate a dashboard (Tableau or Power BI) version of visuals.
    - Creating a summary report notebook with insights + storytelling.
 
---

## Key Takeaways (so far)
- Clear rise in movie production during the 1990s–2010s.
- Ratings distribution is skewed around 6–7, not bell-shaped.
- Certain genres dominate the dataset more than others.
- Audience ratings have gradually declined over the past decades.
- Larger budgets often correlate with higher revenues, though with significant
  variability.
- A handful of directors (e.g., Spielberg, Scorseses, Coppola) consistently
  combine strong output with high average IMDb ratings. 
