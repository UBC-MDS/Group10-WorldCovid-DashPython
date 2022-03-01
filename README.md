# World COVID-19 Dashboard (Python)

## Overview

The World COVID-19 Dashboard is an interactive app that allows users to explore global COVID-19 indicators. The intent of this app is for users to quickly observe and understand the current state of the pandemic situation globally, and compare different metrics across different countries. As we all adjust to living with COVID-19, our dashboard serves as a tool that can clearly demonstrate the movement of the pandemic over time through data summaries and visualizations.

Design:

Our app is centred by a world map showing covid indicators across the globe. The left-hand side of the dashboard contains the main variable filters that users can select to visually present the data across different countries in the world. There are two filters here:
  - the line chart filter, where the user can select two variables for the line chart visualizations on the right of the dashboard, variables like: Confirmed Cases, Deaths, Hospitalizations, ICU's (number of patients in the ICU), Recoveries, and Vaccination Numbers etc; and
  - the country filter, where the user can select which country's data they would like displayed

The top of the app contains our date-time slider, that allows the user to filter for a particular time period they would like to see, the map filter (the blue filter), which controls which feature is showcased in the centre map, and our two data filters:
  - a logarithmic or linear data filter; and
  - a filter for the level of granularity: daily, monthly, or weekly

The detailed proposal can be found [here](https://github.com/UBC-MDS/group10-worldcovid-dashpython/blob/main/docs/proposal.md)

The complete COVID-19 dataset used in our dashboard can be downloaded in [CSV](https://covid.ourworldindata.org/data/owid-covid-data.csv) | [XLSX](https://covid.ourworldindata.org/data/owid-covid-data.xlsx) | [JSON](https://covid.ourworldindata.org/data/owid-covid-data.json) and this is a collection of the COVID-19 data maintained by [_Our World in Data_](https://ourworldindata.org/coronavirus).

## Dashboard Design

![](dashboad_sketch.png)

## License

The World COVID-19 Dashboard was created by Adam Morphy, Kingslin Lv, Thomas Siu, and Kristin Bunyan. It is licensed under the terms of the MIT license.

## Contributors
### Development Lead

| Member        | Github                                            |
|---------------|---------------------------------------------------|
| Adam Morphy   | [adammorphy](https://github.com/adammorphy)       |
| Kingslin Lv   | [Kingslin0810](https://github.com/Kingslin0810)   |
| Kristin Bunyan| [khbunyan](https://github.com/khbunyan)           |
| Thomas Siu    | [thomassiu](https://github.com/thomassiu )         |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/group10-worldcovid-dashpython/blob/main/CONTRIBUTING.md).

## References

COVID-19 Data Repository by [Our World Data](https://ourworldindata.org/coronavirus) at University of Oxford. This data has been collected, aggregated, and documented by Cameron Appel, Diana Beltekian, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Lucas Rodés-Guirao, and Max Roser.
