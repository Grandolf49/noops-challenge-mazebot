# Libraries
import queue
import constants as con


def solve_maze(maze, start_pos, end_pos):
    # Finding the number of steps
    count = 0
    no_of_steps = 0
    maze_len = len(maze)
    queue_maze = queue.Queue(maze_len ** 5)
    first_cell = [start_pos[0], start_pos[1], count]
    queue_maze.put(first_cell)
    flag = 0
    count1 = 0
    while not queue_maze.empty():
        cell = queue_maze.get()
        r = cell[1]
        c = cell[0]
        current_level = cell[2]
        print(current_level)
        count1 += 1
        maze[r][c] = str(current_level)
        if r == end_pos[1] and c == end_pos[0]:
            flag = 1
            no_of_steps = current_level
            break
        else:
            if c + 1 < maze_len and (maze[r][c + 1] == con.EMPTY or maze[r][c + 1] == con.DESTINATION):
                next_cell = [c + 1, r, current_level + 1]
                queue_maze.put(next_cell)
            if r + 1 < maze_len and (maze[r + 1][c] == con.EMPTY or maze[r + 1][c] == con.DESTINATION):
                next_cell = [c, r + 1, current_level + 1]
                queue_maze.put(next_cell)
            if c - 1 > -1 and (maze[r][c - 1] == con.EMPTY or maze[r][c - 1] == con.DESTINATION):
                next_cell = [c - 1, r, current_level + 1]
                queue_maze.put(next_cell)
            if r - 1 > -1 and (maze[r - 1][c] == con.EMPTY or maze[r - 1][c] == con.DESTINATION):
                next_cell = [c, r - 1, current_level + 1]
                queue_maze.put(next_cell)
    if flag:
        print('Shortest Path Found!', 'Steps:', no_of_steps)
    else:
        print('No path found!')

    path = ''
    current_cell = [end_pos[1], end_pos[0]]
    for i in range(no_of_steps, 0, -1):
        row = current_cell[0]
        col = current_cell[1]

        if col + 1 < maze_len and maze[row][col + 1] == str(i - 1):
            current_cell = [row, col + 1]
            path += con.WEST
            continue
        if row + 1 < maze_len and maze[row + 1][col] == str(i - 1):
            current_cell = [row + 1, col]
            path += con.NORTH
            continue
        if col - 1 > -1 and maze[row][col - 1] == str(i - 1):
            current_cell = [row, col - 1]
            path += con.EAST
            continue
        if row - 1 > -1 and maze[row - 1][col] == str(i - 1):
            current_cell = [row - 1, col]
            path += con.SOUTH
            continue

    path = path[::-1]
    return path
