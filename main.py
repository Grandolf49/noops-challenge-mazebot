# Libraries
import requests
import queue

# Constants
MAZE_MIN_SIZE = 10
MAZE_MAX_SIZE = 10
PUZZLE_BASE_URL = 'https://api.noopschallenge.com'
PUZZLE_URL = 'https://api.noopschallenge.com/mazebot/random'

# Strings
STR_MIN_SIZE = 'minSize'
STR_MAX_SIZE = 'maxSize'
STR_MAZE_PATH = 'mazePath'
STR_MAP = 'map'
STR_DIRECTIONS = 'directions'
STR_START_POS = 'startingPosition'
STR_END_POS = 'endingPosition'
EMPTY = ' '
OBSTACLE = 'X'
VISITED = '0'
DESTINATION = 'B'

# Directions
EAST = 'E'
WEST = 'W'
NORTH = 'N'
SOUTH = 'S'
# HTTP Request Parameters
params = {STR_MIN_SIZE: MAZE_MIN_SIZE, STR_MAX_SIZE: MAZE_MAX_SIZE}

# Getting data from the API
r = requests.get(PUZZLE_URL, params=params)
data = r.json()
maze_path = data[STR_MAZE_PATH]
maze = data[STR_MAP]
start_pos = data[STR_START_POS]
end_pos = data[STR_END_POS]
maze_len = len(maze)

#print(str(maze), "\n", 'Start:', str(start_pos), "\n", 'End:', str(end_pos), '\n', 'Maze Path:', maze_path)

# Finding the number of steps
count = 0
no_of_steps = 0
queue_maze = queue.Queue(maze_len ** 2)
first_cell = [start_pos[0], start_pos[1], count]
queue_maze.put(first_cell)
flag = 0

#print('Traversing the maze...')
while not queue_maze.empty():
    cell = queue_maze.get()
    r = cell[1]
    c = cell[0]
    current_level = cell[2]
    maze[r][c] = str(current_level)
    if r == end_pos[1] and c == end_pos[0]:
        flag = 1
        no_of_steps = current_level
        break
    else:
        if c + 1 < maze_len and (maze[r][c + 1] == EMPTY or maze[r][c + 1] == DESTINATION):
            next_cell = [c + 1, r, current_level + 1]
            queue_maze.put(next_cell)
        if r + 1 < maze_len and (maze[r + 1][c] == EMPTY or maze[r + 1][c] == DESTINATION):
            next_cell = [c, r + 1, current_level + 1]
            queue_maze.put(next_cell)
        if c - 1 > -1 and (maze[r][c - 1] == EMPTY or maze[r][c - 1] == DESTINATION):
            next_cell = [c - 1, r, current_level + 1]
            queue_maze.put(next_cell)
        if r - 1 > -1 and (maze[r - 1][c] == EMPTY or maze[r - 1][c] == DESTINATION):
            next_cell = [c, r - 1, current_level + 1]
            queue_maze.put(next_cell)

if flag:
    print('Shortest Path Found!', 'Steps:', no_of_steps)
else:
    print('No path found!')
#print('Maze', maze)

# Finding the Path
path = ''
current_cell = [end_pos[1], end_pos[0]]
#print('Finding the path')
for i in range(no_of_steps, 0, -1):
    # print(current_cell)
    row = current_cell[0]
    col = current_cell[1]

    if col + 1 < maze_len and maze[row][col + 1] == str(i - 1):
        current_cell = [row, col + 1]
        path += WEST
        continue
    if row + 1 < maze_len and maze[row + 1][col] == str(i - 1):
        current_cell = [row + 1, col]
        path += NORTH
        continue
    if col - 1 > -1 and maze[row][col - 1] == str(i - 1):
        current_cell = [row, col - 1]
        path += EAST
        continue
    if row - 1 > -1 and maze[row - 1][col] == str(i - 1):
        current_cell = [row - 1, col]
        path += SOUTH
        continue

path = path[::-1]
print(path)
#print(len(path))

# Posting data to API
params = {STR_DIRECTIONS: str(path)}
r = requests.post(url=PUZZLE_BASE_URL + maze_path, json=params)
data = r.json()
print(data)
