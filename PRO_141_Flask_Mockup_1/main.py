from flask import Flask, jsonify, request
import pandas as pd
from ast import literal_eval

app = Flask(__name__)

liked_movies = []
not_liked_movies = []

df = pd.read_csv('My_Movie_Data_Bollywood.csv')
all_movies = df.values.tolist()


@app.route('/')
def index():
    return "Index Page"


@app.route('/get-first-movie', methods=['GET'])
def first_movie():
    return jsonify({
        "Movie ID": all_movies[0][0],
        "Title": all_movies[0][1],
        "Weighted Rating": all_movies[0][2],
        "Director(s)": literal_eval(all_movies[0][3]),
        "Cast": literal_eval(all_movies[0][4]),
        "Genre": literal_eval(all_movies[0][5])
    })

@app.route('/liked-movie', methods=["POST"])
def liked_movie():
    temp_movie_liked_id = int(request.json.get('movie_id'))
    liked_movies.append(df[df['Movie_ID'] == temp_movie_liked_id].values.tolist()[0])
    all_movies.pop(([movie[0] for movie in all_movies if movie[0] == temp_movie_liked_id])[0])
    return jsonify({"message" : "success(Movie Liked)"})

@app.route('/not-liked-movie', methods=["POST"])
def not_liked_movie():
    temp_movie_not_liked_id = int(request.json.get('movie_id'))
    not_liked_movies.append(df[df['Movie_ID'] == temp_movie_not_liked_id].values.tolist()[0])
    all_movies.pop(([movie[0] for movie in all_movies if movie[0] == temp_movie_not_liked_id])[0])
    return jsonify({"message" : "success(Movie Diliked)"})

if __name__ == "__main__":
    app.run(debug=True)