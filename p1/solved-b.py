import plotly.graph_objects as go
import pandas as pd

# df = pd.read_csv(r"file:///C:/Users/20106/Downloads/data-drecov.csv")

df = pd.read_csv(r"data-drecov.csv")

fig = go.Figure(data=go.Choropleth(
    locations = df['countryterritoryCode'],
    z = df['cases'],
    text = df['countriesAndTerritories'],
    colorscale = 'Rainbow',
    autocolorscale=True,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))

fig.update_layout(
    title_text='2014 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
         
        showarrow = False
    )]
)
fig.write_html('first_figure.html', auto_open=True)

fig.show()