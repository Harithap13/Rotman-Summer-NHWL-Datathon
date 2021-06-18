from flask import Flask, request, render_template, url_for, redirect, send_file, make_response, send_from_directory
from werkzeug.utils import secure_filename
from flask import send_from_directory, current_app
import io
import pandas as pd
import numpy as np
import pickle
import joblib
import os
from sklearn.model_selection import train_test_split
import sys
from numpy import zeros, newaxis
import socket
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt




UPLOAD_FOLDER = '/Users/prakritiailavadi/Desktop/post_grad/nwhl_datathon/folder'


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
FLASK_DEBUG = 1

to_predict = ""


@app.route("/")
def index(user=None):
    # var = pickle.load(open('ahe_rf_age_gender.sav', 'rb'))
    return render_template("homepage.html", user=user)


# open start modelling main page
@app.route("/start", methods=['GET', 'POST'])
def start():
    # shock/ahe
    # SubDirectory.script.printfunction("Hello world")
    if request.method == 'POST':
        global to_predict
        to_predict = request.form['to_predict']

    return render_template("startModelling.html")


@app.route('/upload_file_nwhl', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        nwhl_df = pd.read_csv(request.files.get('file'))
        file = request.files['file']
        filename = secure_filename(file.filename)

        return render_template("startModelling.html", data_frame=nwhl_df.to_html())


@app.route("/show_stats_page")
def show_stats_page():
    return render_template("features.html")


@app.route("/calculate_stats")
def calculate_stats():
    # if flag == "file_upload":
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], "all_stats_for_demonstration.csv"))
    df = df.loc[:, ~df.columns.str.contains('Unnamed')]

    return render_template("features.html", features=df.to_html())


@app.route("/show_player")
def show_player():
    return render_template("player.html")


@app.route("/load_player_profile", methods=['GET', 'POST'])
def load_player():
    #image = mpimg.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'Mikyla Profile.png'))

    return render_template("player_profile_selected.html")


if __name__ == "__main__":
    app.run(debug=True)

