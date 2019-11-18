# Libraries
import requests
import constants as con


# Get a random maze from API
def get_random_maze():
    params = {con.STR_MIN_SIZE: con.MAZE_MIN_SIZE, con.STR_MAX_SIZE: con.MAZE_MAX_SIZE}
    r = requests.get(con.PUZZLE_URL, params=params)
    data = r.json()
    return data


# Post the result to API
def post_result_directions(path, maze_path):
    params = {con.STR_DIRECTIONS: str(path)}
    r = requests.post(url=con.PUZZLE_BASE_URL + maze_path, json=params)
    data = r.json()
    return data
