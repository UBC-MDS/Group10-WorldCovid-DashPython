from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import locale
import altair as alt
import datetime
import pandas as pd
from utility import get_data, filter_data
import plotly.graph_objects as go
import plotly_express as px
from datetime import datetime

alt.data_transformers.disable_max_rows()

df = get_data()
daterange = [x for x in range(len(df["date"].unique()))]

marks = {
    numd: date.strftime("%Y-%m-%d")
    for numd, date in zip(daterange, df["date"].dt.date.unique())
}

marks_display = {}
marks_display.update(
    {
        0: {
            "label": datetime.strptime(marks.get(0), "%Y-%m-%d").strftime("%y-%m-%d"),
            "style": {
                "color": "#77b0b1",
            },
        }
    }
)

last_index = len(marks) - 1

for key, item in marks.items():
    if key != 0 and key % 60 == 0 and last_index - key > 30:
        marks_display.update(
            {
                key: {
                    "label": datetime.strptime(item, "%Y-%m-%d").strftime("%y-%m-%d"),
                    "style": {
                        "color": "#77b0b1",
                    },
                }
            }
        )


marks_display.update(
    {
        last_index: {
            "label": datetime.strptime(marks.get(last_index), "%Y-%m-%d").strftime(
                "%y-%m-%d"
            ),
            "style": {
                "color": "#77b0b1",
            },
        }
    }
)

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
    ],
    style={
        "height": "40px",
        "backgroundColor": "white",
    },
)

feature_dropdown_2 = dcc.Dropdown(
    id="feature_dropdown_2",
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
    ],
    style={
        "border-width": "0",
        "height": "40px",
        "backgroundColor": "white",
    },
)

# Date slider
date_slider = dcc.RangeSlider(
    id="date_slider",
    min=daterange[0],
    max=daterange[-1],
    value=[daterange[0], daterange[-1]],
    marks=marks_display,
)

# Data scale radio button
scale_radio = dbc.RadioItems(
    options=[
        {"label": "Linear", "value": "linear"},
        {"label": "Log", "value": "symlog"},
    ],
    value="linear",
    id="scale-radio",
    inline=True,
)

# Country selector
country_selector = dcc.Dropdown(
    id="country-selector",
    multi=True,
    options=[{"label": x, "value": x} for x in df.location.sort_values().unique()],
    value=["Canada", "United States", "United Kingdom"],
)

# Sidebar
sidebar = dbc.Col(
    [
        html.Br(),
        html.H3(
            "World Covid-19 Dashboard",
        ),
        html.Br(),
        html.P(
            "Filter charts with following:",
            style={"font-size": "20px"},
        ),
        html.Hr(),
        html.B("Data Scale:"),
        html.Br(),
        html.Br(),
        scale_radio,
        html.Br(),
        html.Br(),
        html.B("Country:"),
        html.Br(),
        html.Br(),
        country_selector,
        html.Br(),
        html.Br(),
        html.B("Features:"),
        html.Br(),
        html.Br(),
        feature_dropdown,
    ],
    width=3,
    style={
        "border-width": "0",
        "backgroundColor": "#A0C0C6",
        # "min-height": "100vh",
        # "min-width": "1300px",
    },
)

# Map Tab
map_tab = dbc.Col(
    [
        dbc.Row(
            [
                html.P(" "),
                html.Br(),
                html.Br(),
                html.B(id="date_display"),
                html.Br(),
                html.Br(),
                date_slider,
                html.Br(),
                html.Br(),
                html.P(
                    "Animated World Map:",
                    style={"font-size": "25px"},
                ),
                dcc.Graph(
                    id="map_plot",
                    style={"height": "70vh"},
                ),
                html.Br(),
                html.Br(),
                html.P(
                    "Compliment Line Plot:",
                    style={"font-size": "25px"},
                ),
                dbc.Col(
                    html.P(
                        " ",
                    ),
                    width=3,
                ),
                dbc.Col(
                    html.Iframe(
                        id="map_line_chart",
                        style={
                            "height": "70vh",
                            "width": "100%",
                            "textAlign": "center",
                        },
                    ),
                ),
            ]
        ),
    ]
)

# Setup app and layout/ frontend
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

server = app.server

app.layout = dbc.Container(
    dbc.Row(
        [
            sidebar,
            dbc.Col(
                [
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                map_tab,
                                label="Map",
                                tab_id="map-tab",
                            ),
                            dbc.Tab(
                                # feature_dropdown_2,
                                label="Charts",
                                tab_id="charts-tab",
                            ),
                        ]
                    )
                ],
                # style={"width": "80%"},
            ),
        ]
    ),
    fluid=True,
)


# app.layout = dbc.Container(
#     [
#         html.H1(
#             "World Covid-19 App",
#             style={
#                 "border-width": "1",
#                 "width": "100%",
#                 "border-bottom-style": "solid",
#                 "border-bottom-color": "black",
#             },
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [

#                     ],
#                     md=2,
#                     style={"border-width": "1", "width": "100%"},
#                 ),
#                 dbc.Col(
#                     [
#                         html.H5("Date Range Slider"),
#                         dcc.RangeSlider(
#                             id="date_slider",
#                             min=daterange[0],
#                             max=daterange[-1],
#                             value=[daterange[0], daterange[-1]],
#                             step=1,
#                             # tooltip={"placement": "bottom", "always_visible": True},
#                             marks=marks_display,
#                         ),
#                     ],
#                     style={"border-width": "0"},
#                 ),  ## 'border-width': '1', 'width': '100%', 'border-style': 'solid', 'border-color': 'black'
#             ],
#             style={"border-width": "0", "width": "100%"},
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         html.H5("Linear/Log Selector"),
#                         dcc.RadioItems(
#                             id="scale_radio",
#                             options=[
#                                 {"label": "Linear", "value": "linear"},
#                                 {"label": "Log", "value": "symlog"},
#                             ],
#                             value="linear",
#                         ),

#                         html.H5("Country Selector"),
#                         dcc.Dropdown(
#                             id="country_select",
#                             multi=True,
#                             options=[
#                                 {"label": x, "value": x}
#                                 for x in df.location.sort_values().unique()
#                             ],
#                             value=[
#                                 "Canada",
#                                 "World",
#                             ],
#                         ),
#                     ],
#                     md=2,
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Tabs(
#                             [
#                                 dcc.Tab(
#                                     dbc.Col(
#                                         [
#                                             feature_dropdown,
#                                             dcc.Graph(
#                                                 id="map_plot",
#                                                 figure={},
#                                                 style={"height": "70vh"},
#                                             )
#                                         ]
#                                     ),
#                                     label="World Map",
#                                 ),
#                                 dcc.Tab(
#                                     dbc.Col(
#                                         [
#                                             feature_dropdown_2,
#                                             html.Iframe(
#                                                 id="line_plot",
#                                                 style={
#                                                     "border-width": "0",
#                                                     "width": "100vh",
#                                                     "height": "70vh",
#                                                 },
#                                             ),
#                                         ]
#                                     ),
#                                     label="COVID-19 Indicators",
#                                 ),
#                                 dcc.Tab(
#                                     label="Vaccination Indicators",
#                                 ),
#                             ],
#                             style={"width": "100%"},
#                         ),
#                         html.H5("Date selected"),
#                         html.Div(id="date_from_display"),
#                         html.Div(id="date_to_display"),
#                     ],
#                     style={
#                         "border-width": "0",
#                         "width": "90%",
#                         "backgroundColor": "white",
#                         "float": "right",
#                     },
#                 ),
#             ]
#         ),
#     ],
#     style={
#         "border-width": "0",
#         "backgroundColor": "#72a0c1",
#         "min-height": "100vh",
#         "min-width": "1300px",
#     },
# )

# Map plot sample
@app.callback(
    Output("map_plot", "figure"),
    [
        Input("feature_dropdown", "value"),
        Input("country-selector", "value"),
        Input("date_slider", "value"),
        # Input("scale_radio", "value"),
    ],
)
def plot_map(ycol, countries, daterange):

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
        color_continuous_scale=px.colors.sequential.deep,
    )

    fig.update_layout(
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
    )

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 50

    return fig


# Map line chart
@app.callback(
    Output("map_line_chart", "srcDoc"),
    [
        Input("feature_dropdown", "value"),
        Input("country-selector", "value"),
        Input("date_slider", "value"),
        Input("scale-radio", "value"),
    ],
)
def plot_map_line_chart(ycol, countries, daterange, scale):

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
        .properties(width=570, height=300, title=f"Country Data for {ycol}")
        .add_selection(click)
        .interactive()
        .configure_title(
            fontSize=15,
            anchor="start",
        )
    )

    return chart.to_html()


@app.callback(Output("date_display", "children"), Input("date_slider", "value"))
def update_output(value):
    template = "Date range: {} to {}"

    if value is None:
        value = []
        value.append(0)
        value.append(list(marks.keys())[-1])

    output_string = template.format(marks.get(value[0]), marks.get(value[1]))

    return output_string


if __name__ == "__main__":
    app.run_server(debug=True)
