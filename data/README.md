# Data

**Online News Popularity** — UCI Machine Learning Repository  
https://archive.ics.uci.edu/dataset/332/online+news+popularity

- 39,644 Mashable articles, 58 predictive features + `shares` (target source)
- Original file: `OnlineNewsPopularity.csv` (column names contain leading spaces; the notebook strips them)
- License: CC BY 4.0 (see the UCI page)

Place `OnlineNewsPopularity.csv` in this folder, or run:

```bash
python scripts/download_data.py
```

The notebook first tries to download the data from UCI and falls back to `data/OnlineNewsPopularity.csv`.

**Citation:** K. Fernandes, P. Vinagre, P. Cortez. *A Proactive Intelligent Decision Support System for Predicting the Popularity of Online News.* EPIA 2015.
