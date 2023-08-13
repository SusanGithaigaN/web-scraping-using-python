import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# get url contents
data = requests.get(URL)
soup = BeautifulSoup(data.content, 'lxml')
# create a list to store movies
movies = []
# find all: <h3 class="title">95)</h3>

movie_title = soup.find_all('h3', attrs={'class': 'title'})
# print(movie_title)

# get text inside tags
for show in movie_title:
    # print(show.getText().strip())
    all_shows = show.getText().strip()
    # append all movies to our movies array
    movies.append(all_shows)

# write all_shows into text file, add new line after each show
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(movie + "\n")
