## IMDb End-to-End Data Analysis
An end-to-end analysis of IMDb movie data, combining SQL, Python, and visualization to uncover trends in ratings, genres, budgets, and box-office performance. This project demonstrates how to take raw, unstructured data and transform it into actionable insights, simulating a real-world data workflow. 

---

## Structure 
```
├── data_raw/ # Original source files (CSV, SQLite)
├── data_processed/ # Cleaned & transformed outputs (Parquet, CSV)
├── notebooks/ # Jupyter notebooks for EDA & profiling
├── scripts/ # Python ETL and processing scripts
├── visuals/ # Saved plots and figures
├── requirements.txt # Project dependencies
└── README.md # Documentation
```

---

## Objectives
- Build a reproducible ETL pipeline for raw IMDb data.
- Perform data cleaning/transformation.
- Explore the data through EDA and visualizations.
- Present findings in a way that simulates real-world deliverables.

---

## Current Analysis and Visuals

### Trends Over Time
- Movies per Decade (with and without labels)
- Ratings by Year (average IMDb ratings over time)
- Budget vs. Revenue by Year (line chart comparison)


### Sample Visuals 
**Movies Per Decade**
![Movies per Decade](visuals/movies_per_decade.png)

**Top Directors by Avg IMDb Ratings**
![Directors Ratings](visuals/top_directors.png)


**Distribution**
- Movies per Genre (distribution)
- Runtime Distribution (histogram of movie lengths)

**Entity-Level Analysis**
- Top Actors by Film Count
- Directors: Quality and Quantity (ratings vs. film counts)

**Performance Drivers**
- Exploring budget/revenue relationships and rating drivers.
  
---

## Exported Aggregates
- `agg_ratings_by_year.csv`
- `agg_ratings_by_decade.csv`
- `agg_top_actors.csv`

These outputs can be directly reused for dashboards in Tableau, Power BI, or Excel. 


---

## Tools and Libraries
- Python: pandas, matplotlib, seaborn
- SQLite: for structured querying
- Jupyter Notebook: EDA and documentation
- VS Code: Development environment

---

## Future Additions
- Expand SQL queries for deeper exploration.
- Refine decade-level visuals (e.g., adding more comparisons). 
- Incorporate dashboards in Tableau or Power BI for interactive exploration.
- Perform deeper storytelling analysis around trends (e.g., genre evolution,
  box office success drivers).
- Refine README with visuals, insights, and project flow.
- Create a summary report notebook with insights and storytelling.
 
---

## Key Takeaways (so far)
- Clear rise in movie production during the 90's-2010s.
- Average IMDb ratings hover around 6.7-7.0, but vary by decade.
- Directors like Christopher Nolan and Stanley Kubrick consistently deliver
  highly-rated films.
  
---

## How to Run
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the ETL process: ```python scripts/01_clean_transform.py```
4. Open notebooks to explore analysis:
   - `notebooks/01_data_profile.ipynb` - Dataset profiling & sanity checks.
   - `notebooks/02_classic_analysis.ipynb - SQL queries, visuals and exports. 
    
