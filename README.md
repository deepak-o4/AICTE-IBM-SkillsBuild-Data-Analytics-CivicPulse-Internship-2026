# CivicPulse — BBMP Grievance Intelligence

CivicPulse is a historical civic analytics project built on BBMP grievance data for 2020–2024. It converts raw municipal complaint records into ward-wise demand, category trends, operational status analysis, and strategic decision-support insights.

## Project overview
This project maps complaint intensity, service patterns, and ward-level performance to municipal planning priorities. It is designed as a data analytics and dashboard project for the AICTE / IBM SkillsBuild internship track.

## Problem statement
Municipal grievance data is available as raw records but is difficult to interpret at scale. Without structured analysis, civic departments cannot quickly identify recurring problem categories, high-demand wards, or service bottlenecks impacting public experience.

## Objectives
- Analyse annual complaint trends from 2020–2024
- Identify ward-wise and category-wise demand concentrations
- Evaluate grievance status distribution and service outcomes
- Build a dashboard for decision support
- Apply K-Means ward segmentation where justified
- Produce project documentation and reproducible analytical workflows

## Dataset
Source: BBMP grievance data files provided in the project input set.

Coverage: 2020, 2021, 2022, 2023, 2024

Files are stored under:
- `data/raw/`

Processed output:
- `data/processed/bbmp_grievances_clean.csv`
- `data/processed/civicpulse_summary.json`

## Methodology
1. Load all annual CSV files
2. Validate schema and detect duplicate complaint IDs
3. Normalize strings and clean inconsistent data
4. Convert grievance dates into analysis features
5. Build ward, category, status, and time-based aggregates
6. Create KPI metrics and visual outputs
7. Run ward clustering using K-Means
8. Generate a dashboard and project report

## Key findings from the generated analysis
- Electrical complaints are the dominant complaint category across the period.
- Solid Waste (Garbage) Related and Road Maintenance(Engg) are the next highest complaint groups.
- The most complaint-heavy ward is Jnanabharathi Ward, followed by Rajarajeshwari Nagar and Horamavu.
- Grievance volume is highest in recent years and reflects sustained public demand concentration.

## Project structure
```text
CivicPulse/
├── data/
│   ├── raw/
│   └── processed/
├── dashboard/
│   └── app.py
├── outputs/
│   ├── figures/
│   └── tables/
├── src/
│   └── civicpulse_pipeline.py
├── DeepakDubey_CivicPulse.py
├── DeepakDubey_CivicPulse.ipynb
├── DeepakDubey_CivicPulse_ProjectReport.docx
├── requirements.txt
├── README.md
├── DATA_DICTIONARY.md
├── PROJECT_DECISIONS.md
├── PROJECT_INPUT_STATUS.md
├── TESTING.md
└── .gitignore
```

## Installation
```bash
cd CivicPulse
python -m pip install -r requirements.txt
```

## Run the analysis pipeline
```bash
cd CivicPulse
python DeepakDubey_CivicPulse.py
```

## Run the dashboard
```bash
cd CivicPulse
streamlit run dashboard/app.py
```

## Technologies used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Plotly
- python-docx

## Limitations
- The dataset is historical and may not include future municipal actions or newly added complaint categories.
- The analysis is based on complaint volume and status records rather than full operational cost data.
- The clustering output is ward-level and descriptive, not causal.

## Future scope
- Add forecasting for complaint volume
- Compare ward trends with demographic or infrastructure indicators
- Build a more detailed municipal action dashboard
- Extend analytics to monthly or seasonal intervention planning

## Author
Deepak Dubey
