# Libraries
import requests
import queue

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
EMPTY = '0'
# HTTP Request Parameters
params = {STR_MIN_SIZE: MAZE_MIN_SIZE, STR_MAX_SIZE: MAZE_MAX_SIZE}

# Getting data from the API
r = requests.get(PUZZLE_URL, params=params)
data = r.json()
maze = data[STR_MAP]
start_pos = data[STR_START_POS]
end_pos = data[STR_END_POS]
maze_len = len(maze)

print(str(maze), "\n", 'Start: ', str(start_pos), "\n", 'End: ' + str(end_pos))

# Solving the puzzle
count = 0
queue_maze = queue.Queue(maze_len ** 2)
queue_maze.put(start_pos)
flag = 0
while not (queue_maze.empty()):
    cell = queue_maze.get()
    y = cell[0]
    x = cell[1]
    if y == end_pos[0] and x == end_pos[1]:
        flag = 1
        break
    else:
        count += 1
        if x + 1 < maze_len and maze[x + 1][y] != EMPTY:
            maze[x + 1][y] = EMPTY
            queue_maze.put([x + 1, y])
        if y - 1 > -1 and maze[x][y - 1] != EMPTY:
            maze[x][y - 1] = EMPTY
            queue_maze.put([x, y - 1])
        if x - 1 > -1 and maze[x - 1][y] != EMPTY:
            maze[x - 1][y] = EMPTY
            queue_maze.put([x - 1, y])
        if y + 1 < maze_len and maze[x][y + 1] != EMPTY:
            maze[x][y + 1] = EMPTY
            queue_maze.put([x, y + 1])
if flag:
    print('Shortest path found!' + "\n" + "Steps: " + str(count))
else:
    print('No path possible')
