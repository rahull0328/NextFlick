# 🎬 Smart Movie Recommendation System

A content-based **movie recommendation system** that suggests movies similar to the one selected by the user.  
Built using a trained model on the [TMDB](https://www.themoviedb.org/) dataset 🎥📊

## ✨ Features

- 📌 Get movie recommendations based on a selected movie
- 🎞 Uses a content-based filtering approach
- 📂 Pre-trained model using TMDb dataset
- ⚡ Fast and simple user interface
- 💡 Helps discover new and similar movies

## 📁 Dataset

- Source: [KAGGLE](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- The dataset includes information like:
  - Movie title
  - Overview/description
  - Genre
  - Cast & crew
  - Popularity and ratings

## ⚙️ Tech Stack

- 🐍 Python
- 📊 Pandas, NumPy
- 📈 Scikit-learn (for model training)
- 💻 Streamlit

## 🚀 How It Works

1. Load the dataset and clean/preprocess it
2. Use text-based features like **overview, genres, keywords, cast, and crew**
3. Convert them into numerical vectors using **TF-IDF / CountVectorizer**
4. Calculate similarity scores using **cosine similarity**
5. Recommend the top N most similar movies to the user


## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahull0328/nextflick.git
   ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the project:

    ```bash
    streamlit run app.py
    ```

## 📌 Future Improvements:

- 🎭 Add user ratings and collaborative filtering

- 🌐 Deploy the project online

- 🔍 Add search functionality for any movie

## 💖 Acknowledgements

- Dataset from The Movie Database [TMDB](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

- Inspired by the concept of content-based recommendation systems