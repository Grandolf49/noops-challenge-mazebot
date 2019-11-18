# Libraries
import requests
import constants as con


# Get a random maze from API
def get_random_maze():
    params = {con.STR_MIN_SIZE: con.MAZE_MIN_SIZE, con.STR_MAX_SIZE: con.MAZE_MAX_SIZE}
    url = con.PUZZLE_BASE_URL + con.PUZZLE_RANDOM_PATH
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


# Post the result to API
def post_result_directions(path, maze_path):
    params = {con.STR_DIRECTIONS: str(path)}
    r = requests.post(url=con.PUZZLE_BASE_URL + maze_path, json=params)
    data = r.json()
    return data


# Start the race with POST
def post_start_race(login):
    params = {con.STR_LOGIN: str(login)}
    url = con.PUZZLE_BASE_URL + con.PUZZLE_RACE_PATH
    r = requests.post(url=url, json=params)
    data = r.json()
    return data


# Get maze in race mode
def get_maze_race_mode(path):
    url = con.PUZZLE_BASE_URL + path
    r = requests.get(url=url)
    data = r.json()
    return data
