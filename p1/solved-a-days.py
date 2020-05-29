# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:57:22 2020

@author: 20106
"""

import plotly.graph_objects as go

import pandas as pd


import plotly.express as px
#df = px.data.gapminder()
# data = pd.read_csv(r"file:///C:/Users/20106/Downloads/data-drecov.csv")
data = pd.read_csv(r"data-drecov.csv")

px.scatter(data, x="cases", y="deaths", animation_frame="year", animation_group="countriesAndTerritories",
           size="deaths" , hover_name="countriesAndTerritories",
           log_x=True, size_max=55, range_x=[100,25000], range_y=[1,2000])

 
#data = pd.read_csv(r"file:///C:/Users/20106/Downloads/data-f.csv")

dates=["1/1/2020" , "1/15/2020" , "1/30/2020" ,"2/15/2020" ,"2/29/2020" , "3/15/2020" , "4/1/2020" ,"4/15/2020"  ,"4/30/2020" ,"5/11/2020" ]

days=[" 1","5","10","15","20","25","31"]

#Make list of conietentss lsa
continents = []
for continent in data["continentExp"]:
    if continent not in continents:
        continents.append(continent)
 
# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

# fill in most of layout
fig_dict["layout"]["xaxis"] = {"range": [ 100, 2000], "title": "deaths"}
fig_dict["layout"]["yaxis"] = {"range":[1,10000],"title": "recovered" }
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 300, "redraw": False},
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
        "prefix": "Days:",
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
day = 1
for continent1 in continents:
    dataset_by_year = data[data["day"] == day]
    dataset_by_year_and_cont = dataset_by_year[
        dataset_by_year["continentExp"] == continent1]

    data_dict = {
        "x": list(dataset_by_year_and_cont["deaths"]),
        "y": list(dataset_by_year_and_cont["Recovered"]),
        "mode": "markers",
        "text": list(dataset_by_year_and_cont["countriesAndTerritories"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 20000,
            #"size": list(dataset_by_year_and_cont["cases"])
        },
        "name": continent1
    }
    fig_dict["data"].append(data_dict)
    
    
    
# make frames
for day in days:
    frame = {"data": [], "name": str(day)}
    for continent1 in continents:
        dataset_by_year = data[data["day"] == int(day)]
        dataset_by_year_and_cont = dataset_by_year[
            dataset_by_year["continentExp"] == continent1]

        data_dict = {
            "x": list(dataset_by_year_and_cont["deaths"]),
            "y": list(dataset_by_year_and_cont["Recovered"]),
            "mode": "markers",
            "text": list(dataset_by_year_and_cont["countriesAndTerritories"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 200000,
               #"size" :list(dataset_by_year_and_cont["deaths"])
                #"size": list(dataset_by_year_and_cont["cases"])
            },
            "name": continent1
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [day],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": day,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict["layout"]["sliders"] = [sliders_dict]

fig = go.Figure(fig_dict)
fig.write_html('first_figure.html', auto_open=True)




fig.show()