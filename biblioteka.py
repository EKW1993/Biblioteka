import random
from datetime import date
from faker import Faker

fake = Faker()

class MediaItem:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self):
        print(f"Now playing: {self.title}")

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Movie(MediaItem):
    def __init__(self, title, release_year, genre):
        super().__init__(title, release_year, genre)

class Series(MediaItem):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        season_str = str(self.season).zfill(2)
        episode_str = str(self.episode).zfill(2)
        return f"{self.title} S{season_str}E{episode_str}"

library = []

def get_movies():
    movies = [item for item in library if isinstance(item, Movie)]
    movies.sort(key=lambda x: x.title)
    return movies

def get_series():
    series = [item for item in library if isinstance(item, Series)]
    series.sort(key=lambda x: x.title)
    return series

def search(title):
    results = [item for item in library if title.lower() in item.title.lower()]
    results.sort(key=lambda x: x.title)
    return results

def generate_views_multiple(count):
    for _ in range(count):
        generate_views()
        library_info()

def generate_views():
    item = random.choice(library)
    views = random.randint(1, 1000)
    item.play()
    item.views += views

def top_titles(content_type, count):
    if content_type == "movies":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = get_movies() + get_series()
    sorted_items = sorted(items, key=lambda x: x.views, reverse=True)
    sorted_items = [item for item in sorted_items if item.views > 0]
    return sorted_items[:count]

def add_season(title, release_year, genre, season, episode_count):
    for episode in range(1, episode_count + 1):
        series = Series(title, release_year, genre, season, episode)
        library.append(series)

def total_episodes(title):
    total = 0
    for item in library:
        if isinstance(item, Series) and item.title == title:
            total += 1
    return total

def library_info():
    print("Biblioteka filmów i seriali")
    movies = get_movies()
    for movie in movies:
        print(f"{movie} - {movie.views} wyświetleń")
    series = get_series()
    for series_item in series:
        print(f"{series_item} - {series_item.views} wyświetleń")

for _ in range(10):
    title = fake.name()
    release_year = random.randint(1990, 2022)
    genre = fake.word()
    movie = Movie(title, release_year, genre)
    library.append(movie)

for _ in range(10):
    title = fake.name()
    release_year = random.randint(1990, 2022)
    genre = fake.word()
    season = random.randint(1, 10)
    episode_count = random.randint(1, 24)
    add_season(title, release_year, genre, season, episode_count)

print("\nWyświetlanie informacji o bibliotece")
library_info()

print("\nGenerowanie odtworzeń treści")
generate_views_multiple(10)

print("\nWyświetlanie najpopularniejszych tytułów")
today = date.today().strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {today}:")
top_titles_list = top_titles("all", 3)
for idx, title in enumerate(top_titles_list, start=1):
    print(f"{idx}. {str(title)} - {title.views} wyświetleń")