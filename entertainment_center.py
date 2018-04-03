# In order to use the web site builder, we must import it into here
import fresh_tomatoes
import requests
import json
import media

CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
KEY = '7748cb6c2d2dbcdba6bcdffb85f5a74d'
language = 'http://api.themoviedb.org/3/movie/268?api_key={key}&language=en'
videos = 'https://api.themoviedb.org/3/movie/268/videos?api_key={key}&language=en'


def _get_json(url):
    r = requests.get(url)
    return r.json()


config = _get_json(CONFIG_PATTERN.format(key=KEY))

# with open('data.json', 'w') as outfile:
#     json.dump(config, outfile)

languageInfo = _get_json(language.format(key=KEY))

# print(languageInfo["original_title"])
# print(languageInfo["overview"])
# url_image = 'http://image.tmdb.org/t/p/original/' + languageInfo["poster_path"]
# print(url_image)
# webbrowser.open(url_image)
# with open('data2.json', 'w') as outfile:
#     json.dump(languageInfo, outfile)

videoContent = _get_json(videos.format(key=KEY))
# print(videoContent)

batman = media.Movie(
    languageInfo["original_title"],
    languageInfo["overview"],
    'http://image.tmdb.org/t/p/original/' + languageInfo["poster_path"],
    'http://youtube.com/watch?v=' + videoContent['results'][0]['key']
)

nacho = media.Movie("Nacho Libre",
                    "When you are a man...sometimes you wear stretchy pants...it's for fun",
                    "http://image.tmdb.org/t/p/original//lNue9evMBzqjWE4tJmUegkep8Qs.jpg",
                    "https://youtu.be/wptRqr6Ma_E")

jumanji = media.Movie("Jumanji: Welcome to the Jungle",
                      "An old classic never goes out of style",
                      "http://image.tmdb.org/t/p/original//bXrZ5iHBEjH7WMidbUDQ0U2xbmr.jpg",
                      "https://youtu.be/2QKg5SZ_35I")

rocky_iv = media.Movie("Rocky IV",
                       "Rocky's back and this time...it's personal",
                       "http://image.tmdb.org/t/p/original//jmvpwgW5M2kduR9zB0q8qGFC4zM.jpg",
                       "https://youtu.be/i_rUNg_eNwE")

panther = media.Movie("Black Panther",
                      "Long live the King",
                      "http://image.tmdb.org/t/p/original//uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
                      "https://youtu.be/xjDjIWPwcPU")

robocop = media.Movie("Robocop",
                      "Part man, part machine, all cop",
                      "http://image.tmdb.org/t/p/original//gtGreTdzYBuQsEwTliEFdTzPleV.jpg",
                      "https://youtu.be/c3W5HUz7vyY")
movie_ID = [batman, nacho, jumanji, rocky_iv, panther, robocop]
# movie_ID = [268, 9353, 353486, 1374, 284054, 5548]
fresh_tomatoes.open_movies_page(movie_ID)
