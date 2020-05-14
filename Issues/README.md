### Issues

1) Saving plotly graphs is not working in conjuntcion with Jenkins

Plolty relies on [orca]('https://github.com/plotly/orca') application to covert plots to images.

```
Orca is an Electron app that generates images and reports of Plotly things like plotly.js graphs, dash apps, dashboards from the command line.
```

Jenkins can't convert plolty plots to images due to orca interaction. There are issue related to python/jenkins environments.


```
Traceback (most recent call last):
  File "analytics.py", line 200, in <module>
    main()
  File "analytics.py", line 166, in main
    fig.write_image(os.path.join(img_dir,"covid_timeseries.png"))
  File "/home/anaconda3/envs/py37_covidenv/lib/python3.7/site-packages/plotly/basedatatypes.py", line 2824, in write_image
    return pio.write_image(self, *args, **kwargs)
  File "/home/anaconda3/envs/py37_covidenv/lib/python3.7/site-packages/plotly/io/_orca.py", line 1776, in write_image
    with open(file, "wb") as f:
```

