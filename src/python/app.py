from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import locale
import altair as alt
import datetime
import pandas as pd
from utility import get_data, filter_data

alt.data_transformers.disable_max_rows()

df = get_data()
daterange = [x for x in range(len(df["date"].unique()))]

marks = {
    numd: date.strftime("%Y-%m-%d")
    for numd, date in zip(daterange, df["date"].dt.date.unique())
}

marks_display = {}
marks_display.update({0: marks.get(0)})

last_index = len(marks) - 1

for key, item in marks.items():
    if key % 60 == 0 and last_index - key > 30:
        marks_display.update({key: item})


marks_display.update({last_index: marks.get(last_index)})

# Setup app and layout/frontend
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div(
    [
        html.Iframe(
            id="scatter",
            style={"border-width": "0", "width": "100%", "height": "400px"},
        ),
        html.Br(),
        html.H4("Data scale"),
        dcc.RadioItems(
            id="scale_radio",
            options=[
                {"label": "Linear", "value": "linear"},
                {"label": "Log", "value": "symlog"},
            ],
            value="linear",
        ),
        html.Br(),
        html.H4("Feature drop down"),
        dcc.Dropdown(
            id="feature_dropdown",
            value="new_cases_per_million",
            options=[{"label": col, "value": col} for col in df.columns],
        ),
        html.Br(),
        dcc.Dropdown(
            id="country_select",
            multi=True,
            options=[
                {"label": x, "value": x} for x in df.location.sort_values().unique()
            ],
            value=["Canada", "Germany", "Japan", "United Kingdom", "United States"],
        ),
        html.Br(),
        html.H4("Date range slider"),
        dcc.RangeSlider(
            id="date_slider",
            min=daterange[0],
            max=daterange[-1],
            value=[daterange[0], daterange[-1]],
            step=1,
            # tooltip={"placement": "bottom", "always_visible": True},
            marks=marks_display,
        ),
        html.Br(),
        html.H4("Date selected"),
        html.Div(id="date_from_display"),
        html.Div(id="date_to_display"),
    ]
)

# Set up callbacks/backend
@app.callback(
    Output("scatter", "srcDoc"),
    [
        Input("feature_dropdown", "value"),
        Input("country_select", "value"),
        Input("date_slider", "value"),
        Input("scale_radio", "value"),
    ],
)
def plot_altair(ycol, countries, daterange, scale):

    if daterange is None:
        daterange.append(0)
        daterange.append(list(marks.keys())[-1])

    filter_df = filter_data(
        df,
        date_from=marks.get(daterange[0]),
        date_to=marks.get(daterange[1]),
        countries=countries,
    )

    filter_df["count"] = filter_df[ycol]

    chart = (
        alt.Chart(filter_df)
        .mark_line()
        .transform_window(
            rolling_mean="mean(count)",
            frame=[-7, 0],
            groupby=["location"],
        )
        .encode(
            y=alt.Y(
                "rolling_mean:Q",
                scale=alt.Scale(domainMin=0, type=scale),
                title=ycol,
            ),
            x="date",
            tooltip=[ycol],
            color=alt.Color("location", scale=alt.Scale(scheme="dark2")),
        )
        .interactive()
    )
    return chart.to_html()


@app.callback(Output("date_from_display", "children"), Input("date_slider", "value"))
def update_output(value):
    if value is None:
        value = []
        value.append(0)
        value.append(list(marks.keys())[-1])
    return "From: {}".format(marks.get(value[0]))


@app.callback(Output("date_to_display", "children"), Input("date_slider", "value"))
def update_output(value):

    if value is None:
        value = []
        value.append(0)
        value.append(list(marks.keys())[-1])
    return "To: {}".format(marks.get(value[1]))


if __name__ == "__main__":
    app.run_server(debug=True)
