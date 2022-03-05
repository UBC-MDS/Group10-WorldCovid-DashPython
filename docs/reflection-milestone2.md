# Reflection

## Progress of the dashboard:

Out team has implemented the <a href=https://worldcovid-dashpy-stg.herokuapp.com>World COVID-19 Dashboard</a> following the majority of our initial design and proposal. Most of our dashboard's functionality is implemented and we also made a number of improvements to resolve certain confusions compared to our initial sketch design. As opposed to present various filters at one tab which might confuse our audiences of how to filter for the data presentation, we re-designed and created three main tabs: Global COVID-19 Map, Global COVID-19 Plot, and Vaccination and Hospitalization Indicators. As for instance, it's ambiguous to have both date range slider and the filter of monthly/weekly/daily/yearly; potentially map and line plots might not be simultaneously driven by the global filter. Subsequently we decided to set up two global filters: the country selector for multiple country selections, and the data range slider. Also, we upgraded our country selector to be easily added or removed instead of rolling a long list of countries. More specifically, for the first tab of global COVID-19 map, an animated global map highlights selected COVID-19 indicators for the filtered countries, for the second tab a line plot depicts the same data in another format for a better visual presentation; for the third tab of vaccination and hospitalizations, controlled by the global filter there are four plots that also can be filtered by a linear or logarithmic data type. Overall, our team is pleased to illustrate the world map that users can interactively view summarized data when moving the cursor on the map for the pointed country. There are some interactions based on filtered data for the map and the line chart. 

## Areas of improvement/enhancement (limitations) for the dashboard:

There are still a few areas that our teams thrive to cover in the next milestone/implementation:
- Potentially improve the country map animation such as removing repetitive date labels on the slider and opting for the singular date
- Allow filtering by time frame for charts showing the trend
- Further adjust each plot legend/presentation and make more data interaction for a better visualization
- Improve the user experience of the dashboard and use more meaningful color to represent the data in the visualization
- Add a time stamp for the last updated data or a link direction to the source code, and so the user can have a general sense of data presented on the dashboard
- Add a smart data interaction for the vaccination and hospitalization indicators 
