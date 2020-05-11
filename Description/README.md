### Project Structure

[Gogs install_link](Goge_Setup.md)

```
── code
│   ├── analytics.py
│   ├── requirements.txt
│   ├── romania-counties.json
│   ├── romania_geo_map.ipynb
│   └── web_crawler.py
├── crawl_execution.txt
├── datasets
│   ├── getCasesByCounty.json
│   ├── getDailyCaseReport.json
│   ├── getDeadCasesByCounty.json
│   ├── getHealthCasesByCounty.json
│   └── romania-counties.json
├── Description
├── Images
│   ├── county_numbers.png
│   ├── covid_timeseries.png
│   ├── covid_trends.png
│   ├── general_stats.png
│   ├── total_county.png
│   ├── total_dead.png
│   ├── total_healed.png
│   └── trends_pcent.png
├── LICENSE
├── private_repo
│   ├── COVID_DATA
│   ├── getCasesByCounty
│   ├── getDailyCaseReport
│   ├── getDeadCasesByCounty
│   └── getHealthCasesByCounty
└── README.md
```

Refs:

**Setup ssh keys:**
* https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
* https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

**Forecast algorithm(Prophet):**
* https://facebook.github.io/prophet/docs/quick_start.html
* https://facebook.github.io/prophet/docs/diagnostics.html

**Plotly graphing library:**

**Setup scatter plots**

* https://plotly.com/python/line-charts/

**Stackoverflow, how to change th background grid color:**

* https://stackoverflow.com/questions/40720305/horizontal-grid-lines-in-plotly-r#40726060

**Matplotlib style maps:**

* https://ramiro.org/notebook/geopandas-choropleth/
* https://matplotlib.org/3.1.0/tutorials/intermediate/gridspec.html#sphx-glr-tutorials-intermediate-gridspec-py

### Fixed issues:

1 - [X] SSH key must not have write rights:

chmod -x .ssh/

```
git pull origin master
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```


 
