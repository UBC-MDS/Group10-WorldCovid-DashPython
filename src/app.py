from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import locale
import altair as alt
import datetime
import pandas as pd
from utility import get_data, filter_data
import plotly.graph_objects as go
import plotly_express as px

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

feature_dropdown = dcc.Dropdown(
    id="feature_dropdown",
    value="new_cases_per_million",
    options=[
        {"label": "Total confirmed cases", "value": "total_cases"},
        {
            "label": "Total confirmed cases per million people",
            "value": "total_cases_per_million",
        },
        {"label": "Daily confirmed cases", "value": "new_cases"},
        {
            "label": "Daily confirmed cases per million people",
            "value": "new_cases_per_million",
        },
        {"label": "Total deaths", "value": "total_deaths"},
        {
            "label": "Total deaths per million people",
            "value": "total_deaths_per_million",
        },
        {"label": "Daily deaths", "value": "new_deaths"},
        {"label": "Daily deaths per million people", "value": "new_deaths_per_million"},
        {"label": "Current ICU patients", "value": "icu_patients"},
        {
            "label": "Current ICU patients per million people",
            "value": "icu_patients_per_million",
        },
        {"label": "Current hospitalisation", "value": "hosp_patients"},
        {
            "label": "Current hospitalisation per million people",
            "value": "hosp_patients_per_million",
        },
        {"label": "Weekly ICU admissions", "value": "weekly_icu_admissions"},
        {
            "label": "Weekly ICU admissions per million people",
            "value": "weekly_icu_admissions_per_million",
        },
        {
            "label": "Weekly hospitalisation admission",
            "value": "weekly_hosp_admissions",
        },
        {
            "label": "Weekly hospitalisation admission per million people",
            "value": "weekly_hosp_admissions_per_million",
        },
        {
            "label": "People fully vaccinated",
            "value": "people_fully_vaccinated",
        },
    ],
    style={
        "border-width": "0",
        "width": "60%",
        "height": "40px",
        "backgroundColor": "white",
    },
)


# Setup app and layout/ frontend
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = dbc.Container(
    [
        html.H1(
            "World Covid App",
            style={
                "border-width": "1",
                "width": "100%",
                "border-bottom-style": "solid",
                "border-bottom-color": "black",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.RadioItems(
                            id="scale_radio",
                            options=[
                                {"label": "Linear", "value": "linear"},
                                {"label": "Log", "value": "symlog"},
                            ],
                            value="linear",
                        )
                    ],
                    md=2,
                    style={"border-width": "0", "width": "100%"},
                ),
                dbc.Col(
                    [
                        html.H5("Date Range Slider"),
                        dcc.RangeSlider(
                            id="date_slider",
                            min=daterange[0],
                            max=daterange[-1],
                            value=[daterange[0], daterange[-1]],
                            step=1,
                            # tooltip={"placement": "bottom", "always_visible": True},
                            marks=marks_display,
                        ),
                    ],
                    style={"border-width": "0"},
                ),  ## 'border-width': '1', 'width': '100%', 'border-style': 'solid', 'border-color': 'black'
            ],
            style={"border-width": "0", "width": "100%"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Country Selector"),
                        dcc.Dropdown(
                            id="country_select",
                            multi=True,
                            options=[
                                {"label": x, "value": x}
                                for x in df.location.sort_values().unique()
                            ],
                            value=[
                                "Canada",
                                "United States",
                                "United Kingdom",
                                "Netherlands",
                                "Ireland",
                                "Italy",
                                "Australia",
                                "China",
                                "Europe",
                                "Asia",
                                "South America",
                                "North America",
                                "Africa",
                                "Oceania",
                                "World",
                            ],
                        ),
                    ],
                    md=2,
                ),
                dbc.Col(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    dbc.Col(
                                        [
                                            feature_dropdown,
                                            dcc.Graph(
                                                id="map_plot",
                                                figure={},
                                                style={"height": "70vh"},
                                            ),
                                            html.Iframe(
                                                id="line_plot",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100vh",
                                                    "height": "70vh",
                                                },
                                            ),
                                        ]
                                    ),
                                    label="Map",
                                ),
                                dcc.Tab("Plots", label="Plot"),
                            ],
                            style={"width": "15%"},
                        ),
                        html.H5("Date selected"),
                        html.Div(id="date_from_display"),
                        html.Div(id="date_to_display"),
                    ],
                    style={
                        "border-width": "0",
                        "width": "90%",
                        "backgroundColor": "white",
                        "float": "right",
                    },
                ),
            ]
        ),
    ],
    style={
        "border-width": "0",
        "backgroundColor": "#72a0c1",
        "min-height": "100vh",
        "min-width": "1300px",
    },
)


# line plot sample
@app.callback(
    Output("line_plot", "srcDoc"),
    [
        Input("feature_dropdown", "value"),
        Input("country_select", "value"),
        Input("date_slider", "value"),
        Input("scale_radio", "value"),
    ],
)
def plot_line(ycol, countries, daterange, scale):

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

    click = alt.selection_multi(fields=["location"], bind="legend")

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
            tooltip=["location", alt.Tooltip(ycol, title="count")],
            color=alt.Color("location"),
            opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
        )
        .add_selection(click)
        .interactive()
    )
    return chart.to_html()


# Map plot sample
@app.callback(
    Output("map_plot", "figure"),
    [
        Input("feature_dropdown", "value"),
        Input("country_select", "value"),
        Input("date_slider", "value"),
        Input("scale_radio", "value"),
    ],
)
def plot_map(ycol, countries, daterange, scale):

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
    filter_df["date_str"] = filter_df["date"].apply(lambda x: str(x))

    fig = px.choropleth(
        data_frame=filter_df,
        locations="iso_code",
        hover_name="location",
        color=ycol,
        animation_frame="date_str",
        animation_group=ycol,
        color_continuous_scale=px.colors.sequential.Sunset_r,
    )

    fig.update_layout(
        title_text="Covid-19 Map",
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
    )

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 50

    return fig


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
