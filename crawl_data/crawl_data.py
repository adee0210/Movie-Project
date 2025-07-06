from typing import List
import requests
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()


url = "https://api.themoviedb.org/3/"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
headers = {"accept": "application/json", "Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_out_put_url(param, url=url):
    try:
        reponse = requests.get(f"{url}{param}", headers=headers)
        reponse.raise_for_status()
        return reponse.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
    except ValueError:
        print("Response is not valid JSON")
    return None


def discover_movie(discover_movie_path: str, start_page: int, end_page: int):
    urls = [
        discover_movie_path.replace("page=", f"page={str(i)}")
        for i in range(start_page, end_page + 1)
    ]
    movie_id_list = []
    for url in urls:
        data = get_out_put_url(url)
        if data:
            data = data["results"]
            for movie in data:
                movie_id_list.append(movie["id"])

        sleep(3)
    return movie_id_list


def movie_details(movie_details_path: str, movie_id_list: List):
    movie_details_list = []
    url_movie_details_list = [
        movie_details_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_details_list:
        data = get_out_put_url(url)
        if data:
            movie_details_list.append(data)
        sleep(3)
    return movie_details_list


def movie_credits(movie_credits_path: str, movie_id_list: List):
    movie_credits_list = []
    url_movie_credits_list = [
        movie_credits_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_credits_list:
        data = get_out_put_url(url)
        if data:
            movie_credits_list.append(data)
        sleep(3)
    return movie_credits_list


def movie_watch_providers(movie_watch_providers_path: str, movie_id_list: List):
    movie_watch_providers_list = []
    url_movie_watch_providers_list = [
        movie_watch_providers_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_watch_providers_list:
        data = get_out_put_url(url)
        if data:
            movie_watch_providers_list.append(data)
        sleep(3)
    return movie_watch_providers_list


def movie_reviews(movie_reviews_path: str, movie_id_list: List):
    movie_reviews_list = []
    url_movie_reviews_list = [
        movie_reviews_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_reviews_list:
        data = get_out_put_url(url)
        if data:
            movie_reviews_list.append(data)
        sleep(3)
    return movie_reviews_list


def movie_keywords(movie_keywords_path: str, movie_id_list: List):
    movie_keywords_list = []
    url_movie_keywords_list = [
        movie_keywords_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_keywords_list:
        data = get_out_put_url(url)
        if data:
            movie_keywords_list.append(data)
        sleep(3)
    return movie_keywords_list


def movie_trailer_videos(movie_trailer_videos_path: str, movie_id_list: List):
    movie_trailer_videos_list = []
    url_movie_trailer_videos_list = [
        movie_trailer_videos_path.replace("movie_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_trailer_videos_list:
        data = get_out_put_url(url)
        if data:
            movie_trailer_videos_list.append(data)
        sleep(3)
    return movie_trailer_videos_list


def movie_people_details(movie_people_details_path: str, movie_id_list: List):
    movie_people_details_list = []
    url_movie_people_details_list = [
        movie_people_details_path.replace("person_id", str(i)) for i in movie_id_list
    ]
    for url in url_movie_people_details_list:
        data = get_out_put_url(url)
        if data:
            movie_people_details_list.append(data)
        sleep(3)
    return movie_people_details_list


discover_movie_path = "discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
movie_details_path = "movie/movie_id?language=en-US"
movie_credits_path = "movie/movie_id/credits?language=en-US"
movie_watch_providers_path = "movie_id/watch/providers"
movie_reviews_path = "movie/movie_id/reviews?language=en-US&page=1"
movie_keywords_path = "movie/movie_id/keywords"
movie_trailer_videos_path = "movie/movie_id/videos?language=en-US"
movie_people_details_path = "person/person_id?language=en-US"
movie_id_list = discover_movie(discover_movie_path, 1, 2)
print(movie_credits(movie_credits_path, movie_id_list))
