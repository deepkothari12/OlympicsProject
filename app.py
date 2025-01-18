from flask import Flask , render_template , request , Response
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FgCanvas
import seaborn as sns
import io
import base64

fig , ax = plt.subplots(figsize= (6,6))


app = Flask(__name__)

@app.route("/")
def intro_page():
    return render_template("intro.html")

@app.route("/Country_analysis")
def index():
    # Generate the Matplotlib plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot([1, 2, 3, 4, 5], [10, 20, 25, 30, 35], marker="o", label="Line Plot")
    ax.set_title("Dynamic Matplotlib Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    ax.grid(True)

    # Render the plot to an in-memory buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)  # Close the figure to free memory

    # Encode the buffer contents as a Base64 string
    plot_url = base64.b64encode(buf.getvalue()).decode("utf8")

    # Pass the Base64 string to the HTML template
    return render_template("Country.html", plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)