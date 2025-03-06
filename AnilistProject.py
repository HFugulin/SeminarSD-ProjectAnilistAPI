import os
import requests
import json
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import textwrap

# Anilist API URL
ANILIST_API_URL = "https://graphql.anilist.co"

TIMESTAMP = datetime.now().strftime("%d-%m-%YT%Hh%Mm%Ss")

DIR_PATH = "raw-data/"
PLOT_DIR = "plots/"

# Ensure the directory exists
os.makedirs(DIR_PATH, exist_ok=True)
os.makedirs(PLOT_DIR, exist_ok=True)

# GraphQL query to fetch trending anime with scores and genres
QUERY = """
query {
  Page(perPage: 10) {
    media(sort: TRENDING_DESC, type: ANIME) {
      title {
        romaji
      }
      averageScore
      popularity
      genres
    }
  }
}
"""

def fetch_trending_anime():
    """Fetch trending anime data from the Anilist API."""
    response = requests.post(ANILIST_API_URL, json={"query": QUERY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def process_data(anime_data):
    """Process API response to extract relevant details."""
    if not anime_data:
        print("No data to process.")
        return None, None

    media_list = anime_data["data"]["Page"]["media"]
    anime_list = []
    genres_list = []
    for media in media_list:
        if media["averageScore"] is not None:
            title = media["title"]["romaji"]
            genres = media["genres"]
            genres_list.extend(genres)  # Collect all genres for counting
            label = f"{title} ({', '.join(genres)})"
            anime_list.append((label, media["averageScore"]))
    
    return anime_list, genres_list

def write_to_file(filename, data):
    """Write data to a file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            file.write(f"{item}\n")

def save_plot(filename):
    """Save the current plot to a file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, bbox_inches="tight")
    plt.close()

def plot_trending_anime(anime_list):
    """Plot trending anime based on average scores and save the plot."""
    if not anime_list:
        print("No data to visualize.")
        return

    titles, scores = zip(*anime_list)

    # Wrap long titles
    wrapped_titles = ["\n".join(textwrap.wrap(title, width=40)) for title in titles]

    plt.figure(figsize=(14, 8))
    plt.barh(wrapped_titles, scores, color="pink")
    plt.xlabel("Average Score", fontsize=12)
    plt.ylabel("Anime (Genres)", fontsize=12)
    plt.title("Top 10 Trending Anime with Average Scores", fontsize=14)
    
    plt.gca().invert_yaxis()  # Invert so highest score is at the top
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=9)
    plt.subplots_adjust(left=0.4)  # Adjust margin to avoid cutting off labels

    
    plot_filename = PLOT_DIR + f"anime-{TIMESTAMP}.png"
    save_plot(plot_filename)
    print(f"Plot saved to {plot_filename}")

def plot_genre_distribution(genres_list):
    """Plot the distribution of genres in the trending anime and save the plot."""
    if not genres_list:
        print("No genres to visualize.")
        return
    
    # Count genre occurrences
    genre_counts = Counter(genres_list)
    
    # Sort genres by frequency
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    genres, counts = zip(*sorted_genres)

    # Plot genre distribution
    plt.figure(figsize=(12, 6))
    plt.barh(genres, counts, color="skyblue")
    plt.xlabel("Frequency")
    plt.ylabel("Genre")
    plt.title("Genre Distribution in Top 10 Trending Anime")
    plt.gca().invert_yaxis()
    
    plot_filename = PLOT_DIR + f"genre-{TIMESTAMP}.png"
    save_plot(plot_filename)
    print(f"Genre distribution plot saved to {plot_filename}")

if __name__ == "__main__":
    data = fetch_trending_anime()
    anime_list, genres_list = process_data(data)
    
    anime_filename = DIR_PATH + f"animes-{TIMESTAMP}.txt"
    genres_filename = DIR_PATH + f"genre-{TIMESTAMP}.txt"
    
    if anime_list:
        write_to_file(anime_filename, anime_list)
    if genres_list:
        write_to_file(genres_filename, genres_list)
    
    if anime_list:
        plot_trending_anime(anime_list)
        plot_genre_distribution(genres_list)