# Reflection

## Progress of the dashboard:

Out team has implemented the <a href=https://worldcovid-dashpy-stg.herokuapp.com>World COVID-19 Dashboard</a> following the majority of our initial design and proposal. Most of our dashboard's functionality is implemented and we also made a number of improvements to resolve certain confusions compared to our original sketch design. As opposed to present various filters at one tab which might confuse our audiences of how to filter for the data presentation, we re-designed and created two main tabs: global interactors and vaccination and hospitalization indicators. As for instance, it's ambiguous to have both date range slider and the filter of monthly/weekly/daily/yearly, or the map and line plots might not be simultaneously driven by the global filter. We decided to have two global filters: the country selector for multiple country selections, and data range slider. Also, we upgraded our country selector to be easily typed in instead of rolling a long list of countries. More specifically, for the first tab of global COVID-19 indicators, an animated global map highlights selected COVID-19 indicators for the filtered countries, and a line plot depicts the same data in another format for a better visual presentation; for the second tab of vaccination and hospitalizations, controlled by the global filter there are four line charts that also can be filtered by a linear or logarithmic data type. Overall, our team is pleased to illustrate the world map that users can interactively view summarized data when moving the cursor on the map for the pointed country. There are some interactions based on filtered data for the map and the line chart. 

## Areas of Improvement/Enhancement (Limitations) for the dashboard:

There are still a few areas that our teams thrive to cover in the next milestone/implementation.
- Potentially improve the country map animation such as removing repetitive date labels on the slider and opting for the singular date
- Allow filtering by time frame for charts showing the trend
- Improve the user experience of the dashboard and use more meaningful color to represent the data in the visualization.
- Add a time stamp for the last updated data, and so the user can have a general sense of when our data is updated on the dashboard or a link direction to the source code.
- Add a smart data interaction for the vaccination and hospitalization indicators 
