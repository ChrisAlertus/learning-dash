# Learning Dash (python-based web app framework)


(september 7th 2018) https://dash.plot.ly/getting-started-part-2

Dash is a library written in python used to create reactive (think responsive 
like excel files) web applications. It also provides the ability to create 
complex data visualizations - given that it is built by the developers of 
plot.ly. 

This set of python files are examples from the official tutorials that explain
"getting started with Dash". It steps form a simple rendering of a static page
through to an interactive visualization using plot.ly without user inputs/
dynamic updating all the way to dynamic pages interactions based on sliders/
other input component types.

My original thought was to play around and figure out how to build two project
UI's:
- A demo visualization for a recommendation engine - originally for item-item 
reco based on selecting some item of interest, dynamically serving option 
reco's and displaying them visually
- A GUI for a clustering tool. Giving users the ability to select attributes
they are interested in focusing on for analysis then on the backend 
running a pipeline that: 
- decorrelates variables 
- runs different, selected clustering algorithms 
- reduces dimensionality and visualises the results 
- produces a table with units assigned to clusters for consumption by user 
(perhaps ablity to download a csv/ excel/write to db with cluster profiles 
/ assignments)
- produce a profile of the clusters based on other attributes pre-specified 
and the variables used to cluster