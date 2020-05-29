# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:03:38 2020

@author: Poline
"""

import plotly.graph_objects as go

import pandas as pd

url = "file:///C:/Users/20106/Downloads/data-drecov.csv"
dataset = pd.read_csv(url)

months = [ "1", "2", "3", "4", "5"]

# make list of continents
continents = []
for continentExp in dataset["continentExp"]:
    if continentExp not in continents:
        continents.append(continentExp)
# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

# fill in most of layout
fig_dict["layout"]["xaxis"] = {"range": [0, 2000], "title": "deaths"}
fig_dict["layout"]["yaxis"] = {"range": [0, 10000],"title": "Recovered"}
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "month:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

# make data
month = 12
for continentExp in continents:
    dataset_by_year = dataset[dataset["month"] == month]
    dataset_by_year_and_cont = dataset_by_year[
        dataset_by_year["continentExp"] == continentExp]

    data_dict = {
        "x": list(dataset_by_year_and_cont["deaths"]),
        "y": list(dataset_by_year_and_cont["Recovered"]),
        "mode": "markers",
        "text": list(dataset_by_year_and_cont["countriesAndTerritories"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 200000,
             "size": list(dataset_by_year_and_cont["pop"])
        },
        "name": continentExp
    }
    fig_dict["data"].append(data_dict)

# make frames
for month in months:
    frame = {"data": [], "name": str(month)}
    for continentExp in continents:
        dataset_by_year = dataset[dataset["month"] == int(month)]
        dataset_by_year_and_cont = dataset_by_year[
            dataset_by_year["continentExp"] == continentExp]

        data_dict = {
            "x": list(dataset_by_year_and_cont["deaths"]),
            "y": list(dataset_by_year_and_cont["Recovered"]),
            "mode": "markers",
            "text": list(dataset_by_year_and_cont["countriesAndTerritories"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 200000,
                 "size": list(dataset_by_year_and_cont["pop"])
            },
            "name": continentExp
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [month],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": month,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict["layout"]["sliders"] = [sliders_dict]

fig = go.Figure(fig_dict)
fig.write_html('first_figure.html', auto_open=True)


fig.show()