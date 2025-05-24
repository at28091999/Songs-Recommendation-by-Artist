from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

song_df = pd.read_csv("dataset_sample.csv")

def recommender(artist_name):
    artist_songs = song_df[song_df["artist"].str.lower() == artist_name.lower()]
    if artist_songs.empty:
        return ["No songs found for that artist."]
    return artist_songs["song"].head(5).tolist()

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None
    if request.method == 'POST':
        artist_name = request.form['artist']
        recommendations = recommender(artist_name)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
