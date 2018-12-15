# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.Dropdown(
        id='continent-dropdown',
        # options=[{'label': k, 'value': k} for k in all_options.keys()],
        options=[{'label': c['continent'], 'value': c['continent']} for c in df.to_dict("rows")],
        value='Asia'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-dropdown'),

    html.Hr(),

    html.Hr(),

    dt.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False} for i in df.columns
        ],
        data= [], #df.to_dict("rows"),
        editable=False,
        filtering=True,
        sorting=True,
        sorting_type="multi",
        row_selectable="multi",
        row_deletable=True,
        selected_rows=[],
    ),

    html.Div(id='display-selected-values')

])


@app.callback(
    dash.dependencies.Output('cities-dropdown', 'options'),
    [dash.dependencies.Input('continent-dropdown', 'value')])
def set_cities_options(selected_continent):
    return [{'label': i, 'value': i}
            for i in df.loc[df.continent == selected_continent, "country"]]


@app.callback(
    dash.dependencies.Output('cities-dropdown', 'value'),
    [dash.dependencies.Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    dash.dependencies.Output('datatable-interactivity', "data"),
    [dash.dependencies.Input('continent-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value')])
def filter_table(selected_continent, selected_country):
    is_continent = df['continent']== selected_continent
    is_country = df['country'] == selected_country
    return df[is_continent & is_country].to_dict("rows")


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('continent-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value')])
def set_display_children(selected_continent, selected_country):
    return u'{} is a country in {}'.format(
        selected_country, selected_continent,
    )

# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)