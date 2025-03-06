import os
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

data_dir = "raw-data/"
plot_dir = "aggregated-plots/"
os.makedirs(plot_dir, exist_ok=True)

TIMESTAMP = datetime.now().strftime("%d-%m-%YT%Hh%Mm%Ss")

def read_data_files():
    anime_counts = Counter()
    genre_counts = Counter()
    anime_titles = set()
    
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if "animes" in filename:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    title, score = line.rsplit(" ", 1)
                    title = title.strip("()")
                    anime_counts[title] += 1
                    anime_titles.add(title)
        elif "genre" in filename:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    genre = line.strip()
                    genre_counts[genre] += 1
    
    return anime_counts, genre_counts, anime_titles

def plot_genre_frequency(genre_counts):
    plt.figure(figsize=(12, 6))
    genres, counts = zip(*genre_counts.most_common())
    plt.barh(genres, counts, color="steelblue")
    plt.xlabel("Frequency")
    plt.ylabel("Genre")
    plt.title("Total Frequency of All Genres")
    plt.gca().invert_yaxis()
    plt.savefig(os.path.join(plot_dir, f"genre_frequency-{TIMESTAMP}.png"), bbox_inches="tight")
    plt.close()

def plot_anime_frequency(anime_counts):
    plt.figure(figsize=(12, 6))
    titles, counts = zip(*anime_counts.most_common())
    plt.barh(titles, counts, color="palevioletred")
    plt.xlabel("Frequency")
    plt.ylabel("Anime Title")
    plt.title("Frequency of Anime in the Top 10")
    plt.gca().invert_yaxis()
    plt.savefig(os.path.join(plot_dir, f"anime_frequency-{TIMESTAMP}.png"), bbox_inches="tight")
    plt.close()

# def plot_all_animes(anime_titles):
#     plt.figure(figsize=(12, 6))
#     plt.barh(list(anime_titles), [1] * len(anime_titles), color="limegreen")
#     plt.xlabel("Appearances")
#     plt.ylabel("Anime Title")
#     plt.title("All Animes That Appeared at Least Once in the Top 10")
#     plt.gca().invert_yaxis()
#     plt.savefig(os.path.join(plot_dir, "all_animes.png"), bbox_inches="tight")
#     plt.close()

if __name__ == "__main__":
    anime_counts, genre_counts, anime_titles = read_data_files()
    plot_genre_frequency(genre_counts)
    plot_anime_frequency(anime_counts)
    # plot_all_animes(anime_titles)
    print("Plots saved in", plot_dir)