# coeus

<h3>Languages</h3>
A QSM (quantitative statistical model) that takes past quantitative data in the form of pastadjusted close prices to predict future stock prices. The majority of the backend of the coeus QSM was written using Python (--v 2.7), with minor PHP (--v 5.6) scripts to handle connecting and pulling data from MySQL relational databases. The frontend is written is basic HTML and CSS markup, with added functionality from JavaScript through the Angular framework. Historical data for this project was pulled using the IEX Finance API, which returned requested data in the form of Pandas DF's(dataframes).

<h3>Libraries and Modules</h3>
The Scikit-learn SDK was used to develop the ML LRM this model utilises. Furthermore, MatPlotLib and its submodule .pyplot are both used for the plotting of historical stock data as well as the predicted outcome of the model. The mpld3 module for python 2.7 is also used for converting the MatPlotLib graphs into interactive web graphs which are to be seen in the top and bottom right hand corners of the final webdashboard. &nbsp;


<img src="https://raw.githubusercontent.com/oyvindjr-sigvaldsen/coeus/master/coeus-webdashboard.png">
