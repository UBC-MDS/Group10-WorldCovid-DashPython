import pandas as pd
from datetime import datetime
import time


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

    df = df.query("@date_from <= date <= @date_to and location in @countries")

    return df.copy()
