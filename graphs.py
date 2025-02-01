from   flask import Flask , render_template , request , Response , url_for
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_agg import FigureCanvasAgg as FgCanvas
import seaborn as sns
import io
import base64


##readDataframe
df = pd.read_csv("final_athlete_file.csv")


##Country filter functionss
def Country_details(Country_name):
        Country_name = Country_name.lower()
        Country_filter = df[df['NOC'] == Country_name]
        #print("Typee --> ", type(sex_count))
        return Country_filter

## Extract year From Drom Down 
def Extract_year():
        year = df['Year'].sort_values()

        return year


##GrphsPlot Library
def graphs_plot_sex(data):
        sex_count = data['Sex'].value_counts()
        fig , ax = plt.subplots(figsize= (5,5))
        plt.bar(x = sex_count.index , height=sex_count.values)
        
        plt.title("Gender Count" , color = 'white' , fontweight="bold")
        plt.xlabel("Gender" , color = 'white' , fontweight="bold")
        plt.ylabel("Count", color = 'white' , fontweight="bold")
        canvas = FgCanvas(figure=fig)
        img = io.BytesIO()
        plt.savefig(img , format = 'png'  , transparent=True)
        img.seek(0)

        graph_url = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode("utf-8")

        return graph_url

##Piee Chartss Of Sexxx
def pie_char_sex(data):
        fig , ax = plt.subplots(figsize= (5,5))
        sex_count = data['Sex'].value_counts()
        plt.pie(x = sex_count , autopct = "%0.1f%%" , labels= sex_count.index)
        plt.title("Percentages Of Male and Female" , color = 'white' , fontweight="bold")
        canvas = FgCanvas(figure=fig)
        img__ = io.BytesIO()
        plt.savefig(img__ , format = 'png'  , transparent=True)
        img__.seek(0)

        pie_chart_sex = "data:image/png;base64," + base64.b64encode(img__.getvalue()).decode("utf-8")
        return pie_chart_sex

def kde_plot_age(data):
        #print("data -->>>" , data)
        fig , ax = plt.subplots(figsize= (5,5))
        sns.histplot(data=data , x = data['Age'] , kde=True)
        plt.title("Disribution of Age" , color = 'white' , fontweight="bold")
        plt.xlabel("Gender" , color = 'white' , fontweight="bold")
        # plt.ylabel("Count")
        canvas = FgCanvas(figure=fig)
        img_age = io.BytesIO()
        plt.savefig(img_age , format = 'png' , transparent=True)
        img_age.seek(0)
        
        age_kde_plot = "data:image/png;base64," + base64.b64encode(img_age.getvalue()).decode("utf-8")
        return age_kde_plot

def kde_plot_height(data):
        fig , ax = plt.subplots(figsize= (5,5))
        sns.histplot(data=data , x = data['Height'] , kde=True)
        plt.title("Disribution of Height" , color = 'white' , fontweight="bold")
        plt.xlabel("Height" , color = 'white' , fontweight="bold")
        # plt.ylabel("Count")
        canvas = FgCanvas(figure=fig)
        img_age = io.BytesIO()
        plt.savefig(img_age , format = 'png' , transparent=True)
        img_age.seek(0)
        
        height_kde_plot = "data:image/png;base64," + base64.b64encode(img_age.getvalue()).decode("utf-8")
        return height_kde_plot


def graph_of_season(data):
        fig, ax = plt.subplots(figsize=(5,5))
        data = data['Season'].value_counts()
        plt.bar(x = data.index , height = data.values)
        plt.xlabel("Season" , color = 'white' , fontweight="bold")
        plt.ylabel("Total Matches" , color = 'white' , fontweight="bold")
        canvas = FgCanvas(figure=fig)
        img_age = io.BytesIO()
        plt.savefig(img_age , format = 'png' , transparent=True)
        img_age.seek(0)
        
        graph_season = "data:image/png;base64," + base64.b64encode(img_age.getvalue()).decode("utf-8")

        return graph_season


## Function for the Season buttons
def Season_wise_data(season_data):
    seasons_data = df[df['Season'] == season_data]
    fig, ax = plt.subplots(figsize=(5,5))
    #data = data['Season'].value_counts()
    city = seasons_data['City'].value_counts().sort_values(ascending = False).head(5)
    plt.bar(x = city.index , height = city.values)
    plt.xlabel("Season" , color = 'white' , fontweight="bold")
    plt.ylabel("Total Matches", color = 'white' , fontweight="bold")
    canvas = FgCanvas(figure=fig)
    img_age = io.BytesIO()
    plt.savefig(img_age , format = 'png' , transparent=True)
    img_age.seek(0)
    
    graph_season_wise = "data:image/png;base64," + base64.b64encode(img_age.getvalue()).decode("utf-8")
    return graph_season_wise


