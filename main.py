import requests

MAZE_MIN_SIZE = 10
MAZE_MAX_SIZE = 20
PUZZLE_URL = 'https://api.noopschallenge.com/mazebot/random'
STR_MIN_SIZE = 'minSize'
STR_MAX_SIZE = 'maxSize'
STR_MAP = 'map'

params = {STR_MIN_SIZE: MAZE_MIN_SIZE, STR_MAX_SIZE: MAZE_MAX_SIZE}

r = requests.get(PUZZLE_URL, params=params)
data = r.json()
maze = data[STR_MAP]

print(maze)
