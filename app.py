from   flask import Flask, render_template, request, Response, url_for, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_agg import FigureCanvasAgg as FgCanvas
import seaborn as sns
import graphs


app = Flask(__name__)

@app.route("/")
def intro_page():
    return render_template("intro.html")

@app.route("/Country_analysis" ,  methods = ['GET' , 'POST'])
def Country_index():
    print("Country Analysis")
    return render_template("Country.html")

@app.route("/country_details"  ,  methods = ['GET' , 'POST'])
def country_details_function_sex_count():
    if request.method == 'POST':

        Country_name = request.form.get("countryInput")
        #print("Country" , Country_name)
        data = graphs.Country_details(Country_name = Country_name)

        # dataFrame = graphs.DataFrame_show(data=Country_name)
        #print("Data --> " , data.head(2))
        graph_url = graphs.graphs_plot_sex(data = data)
        
        ##pie Chart Of Sex
        pie_chart_sex = graphs.pie_char_sex(data=data)
        
        ##age Distribution
        age_kde_plot = graphs.kde_plot_age(data = data)

        ##height_kde_plott
        height_kde_plot = graphs.kde_plot_height(data = data)

        ##season Grpahss
        season_plot = graphs.graph_of_season(data = data)


    return render_template("Country.html", graph = graph_url , Country_name = Country_name.capitalize() ,  # type: ignore
                           kde_age = age_kde_plot, season_plot = season_plot, pie_chart_sex = pie_chart_sex , height_kde_plot = height_kde_plot )

@app.route("/season_data" , methods = ['GET' , 'POST'])
def season_data():
    #if request.method == "POST":
    season_data_values = request.form.get("Season_wise_data")
    Response_from_season_fun = graphs.Season_wise_data(season_data=season_data_values)
    #print(Response_from_season_fun)
    print("Yess there is Some Response")

    
    return render_template("Country.html" , Response_from_season_fun = Response_from_season_fun)

if __name__ == "__main__":
    app.run(debug=True)