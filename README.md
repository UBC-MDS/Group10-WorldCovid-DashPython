# World COVID-19 Dashboard (Python)

## Overview

The World COVID-19 Dashboard is an interactive app that allows users to explore global COVID-19 indicators. The intent of this app is for users to quickly observe and understand the current state of the pandemic situation globally, and compare different metrics across different countries. As we all adjust to living with COVID-19, our dashboard serves as a tool that can clearly demonstrate the movement of the pandemic over time through data summaries and visualizations.

Design:

Our app consists of two main tabs: Global COVID-19 Indicators and Vaccination and Hospitalization Indicators.

Global COVID-19 Indicators:
 - This tab aims to give a "global overview" of the COVID-19 situation. The tab has two main elements, an animated global map that highlights selected countries for the selected indicator and a line plot that depicts the same data in a different format. Both of these visualization elements are filtered using the "Indicator" drop down to select which indicator is visualized, the "Country" filter to select which countries are showcased, and the "Date range" slider at the top of the screen that limits or expands the visiualized timeline. A main focus of this tab is the animation in the map, which shows the change in data over time by country. This element is expecially important as it tells a story of where the world started, where it went, and how far it has come in a very tangible way. The line plot is also filterable by data type: linear or log

Vaccination and Hospitalization:
- This tab aims to give a sense of the movement of vaccinaction rates and hospitalizations, and how that differed between nations throughout the pandemic. It consists of four line charts; total vaccinations by country, current ICU hospitalizations, and current hospitalizations. Simialr to the first tab, the charts are filtered by the "Country" filter to select which countries are showcased, and the "Date range" slider at the top of the screen that limits or expands the visiualized timeline. They can also be filtered by data type: linear or log.

App usage demonstration:
- Per the GIF below, our app is meant to be highly filterable and interactive and can be used multiple ways to suit the data needs of policy makers, and public health communicators in the best way they see fit for the message they want to convey


**add GIF here**




The complete COVID-19 dataset used in our dashboard can be downloaded in [CSV](https://covid.ourworldindata.org/data/owid-covid-data.csv) | [XLSX](https://covid.ourworldindata.org/data/owid-covid-data.xlsx) | [JSON](https://covid.ourworldindata.org/data/owid-covid-data.json) and this is a collection of the COVID-19 data maintained by [_Our World in Data_](https://ourworldindata.org/coronavirus).

## License

The World COVID-19 Dashboard was created by Adam Morphy, Kingslin Lv, Thomas Siu, and Kristin Bunyan. It is licensed under the terms of the MIT license.

## Contributors
### Development Lead

| Member        | Github                                            |
|---------------|---------------------------------------------------|
| Adam Morphy   | [adammorphy](https://github.com/adammorphy)       |
| Kingslin Lv   | [Kingslin0810](https://github.com/Kingslin0810)   |
| Kristin Bunyan| [khbunyan](https://github.com/khbunyan)           |
| Thomas Siu    | [thomassiu](https://github.com/thomassiu)         |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/group10-worldcovid-dashpython/blob/main/CONTRIBUTING.md).

## References

COVID-19 Data Repository by [Our World Data](https://ourworldindata.org/coronavirus) at University of Oxford. This data has been collected, aggregated, and documented by Cameron Appel, Diana Beltekian, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Lucas Rodés-Guirao, and Max Roser.
