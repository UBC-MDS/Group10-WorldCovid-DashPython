import pandas as pd
from datetime import datetime
import time
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


def get_data(date_from=None, date_to=None, location=None):
    """Get covid data
    Retrieve covid data in pandas dataframe format

    Returns
    -------
    pandas.DataFrame
        Pandas dataframe of the selected covid data.

    Examples
    --------
    >>> get_data()
    """
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    try:
        df = pd.read_csv(url, parse_dates=["date"])
    except BaseException:
        return "The link to the data is broken."

    columns = [
        "iso_code",
        "continent",
        "location",
        "date",
        "total_cases",
        "new_cases",
        "total_deaths",
        "new_deaths",
        "total_cases_per_million",
        "new_cases_per_million",
        "total_deaths_per_million",
        "new_deaths_per_million",
        "icu_patients",
        "icu_patients_per_million",
        "hosp_patients",
        "hosp_patients_per_million",
        "weekly_icu_admissions",
        "weekly_icu_admissions_per_million",
        "weekly_hosp_admissions",
        "weekly_hosp_admissions_per_million",
        "total_vaccinations",
        "people_vaccinated",
        "people_fully_vaccinated",
        "new_vaccinations",
        "population",
    ]

    df = df[columns]

    df = df.fillna(value=0)

    df = df[~df["iso_code"].str.startswith("OWID")]

    return df.sort_values("date")


def filter_data(df, date_from=None, date_to=None, countries=None):
    """filter covid data
    Filter covid data in pandas dataframe format
    with the time periods and countries provided.

    Parameters
    ----------
    df : pandas dataframe
        The covid dataframe to filter
    date_from : str, optional
        Start date of the data range with format 'YYYY-MM-DD'.
        By default 'None' is used to represent earliest date available
    date_to : str, optional
        End date of data range with format 'YYYY-MM-DD'.
        By default 'None' is used to represent latest date available
    countries : list, optional
        List of target country names.
        By default 'None' is used for Canada plus United States, United Kingdom, Germany, Singapore.

    Returns
    -------
    pandas.DataFrame
        Pandas dataframe of the selected covid data .

    Examples
    --------
    >>> get_data(date_from="2022-01-01",
                date_to="2022-01-07",
                location=["Canada", "United States"])
    """

    query = "@date_from <= date <= @date_to"

    if date_from is None:
        date_from = df["date"].min()

    if date_to is None:
        date_to = df["date"].max()

    if countries is None:
        countries = [
            "Canada",
            "United States",
            "Germany",
            "United Kingdom",
            "Singapore",
        ]
    elif "all" not in countries:
        query += " and location in @countries"

    df = df.query(query)

    return df.copy()


feature_dropdown = dcc.Dropdown(
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
        #        "width": "60%",
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
        "width": "60%",
        "height": "40px",
        "backgroundColor": "white",
    },
)
