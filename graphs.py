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

def Country_details(Country_name):
        Country_name = Country_name.lower()
        Country_filter = df[df['NOC'] == Country_name]
        #print("Typee --> ", type(sex_count))
        return Country_filter

##GrphsPlot Library
def graphs_plot_sex(data):
        sex_count = data['Sex'].value_counts()
        fig , ax = plt.subplots(figsize= (6,6))
        plt.bar(x = sex_count.index , height=sex_count.values)
        plt.title("Gender Count")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        canvas = FgCanvas(figure=fig)
        img = io.BytesIO()
        plt.savefig(img , format = 'png')
        img.seek(0)

        graph_url = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode("utf-8")

        return graph_url

def kde_plot_age(data):
        #print("data -->>>" , data)
        fig , ax = plt.subplots(figsize= (6,6))
        sns.histplot(data=data , x = data['Age'] , kde=True)
        # plt.title("")
        # plt.xlabel("Gender")
        # plt.ylabel("Count")
        canvas = FgCanvas(figure=fig)
        img_age = io.BytesIO()
        plt.savefig(img_age , format = 'png')
        img_age.seek(0)
        
        age_kde_plot = "data:image/png;base64," + base64.b64encode(img_age.getvalue()).decode("utf-8")
        return age_kde_plot


