import requests

# Constants
MAZE_MIN_SIZE = 10
MAZE_MAX_SIZE = 20
PUZZLE_URL = 'https://api.noopschallenge.com/mazebot/random'

# Strings
STR_MIN_SIZE = 'minSize'
STR_MAX_SIZE = 'maxSize'
STR_MAP = 'map'
STR_START_POS = 'startingPosition'
STR_END_POS = 'endingPosition'

params = {STR_MIN_SIZE: MAZE_MIN_SIZE, STR_MAX_SIZE: MAZE_MAX_SIZE}

r = requests.get(PUZZLE_URL, params=params)
data = r.json()
maze = data[STR_MAP]
start_pos = data[STR_START_POS]
end_pos = data[STR_END_POS]

print(str(maze) + "\n" + str(start_pos) + "\n" + str(end_pos))
