# Libraries
import queue
import constants as con

# Dijkstraj Constants
VISITED = 1
NOT_VISITED = 0


# BFS Implementation
def solve_maze_bfs(maze, start_pos, end_pos):
    # Finding the number of steps
    count = 0
    no_of_steps = 0
    maze_len = len(maze)
    queue_maze = queue.Queue(maze_len ** 2)
    first_cell = [start_pos[0], start_pos[1], count]
    queue_maze.put(first_cell)

    while not queue_maze.empty():
        cell = queue_maze.get()
        r = cell[1]
        c = cell[0]
        current_level = cell[2]
        maze[r][c] = str(current_level)
        if r == end_pos[1] and c == end_pos[0]:
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


def get_min_node(visited, weights, no_of_nodes):
    min_node = 0
    min_weight = 1
    for i in range(no_of_nodes):
        if visited[i] == NOT_VISITED:
            min_node = i
            min_weight = weights[min_node]
            break

    for i in range(no_of_nodes):
        if weights[i] < min_weight and visited[i] == NOT_VISITED:
            min_node = i
            min_weight = weights[min_node]

    return min_node


def get_path(parent, source, destination, size):
    path = []
    while destination != parent[destination]:
        path.append(destination)
        destination = parent[destination]
    path.reverse()

    path_dir = ''
    x = int(source / size)
    y = source % size
    current_pos = [x, y]

    for i in range(len(path)):
        next_pos = [int(path[i] / size), path[i] % size]
        x_pos = current_pos[0] - next_pos[0]
        y_pos = current_pos[1] - next_pos[1]

        if x_pos == 1 and y_pos == 0:
            path_dir += con.NORTH
        if x_pos == 0 and y_pos == -1:
            path_dir += con.EAST
        if x_pos == -1 and y_pos == 0:
            path_dir += con.SOUTH
        if x_pos == 0 and y_pos == 1:
            path_dir += con.WEST

        current_pos[0] = next_pos[0]
        current_pos[1] = next_pos[1]

    return path_dir


# Dijkstraj's Algorithm Implementation
def solve_maze_dijkstraj(maze, start_pos, end_pos):
    size = len(maze)
    no_of_nodes = size ** 2
    all_nodes_visited = no_of_nodes

    source = start_pos[1] * size + start_pos[0]
    destination = end_pos[1] * size + end_pos[0]

    visited = [NOT_VISITED for x in range(no_of_nodes)]
    weights = [no_of_nodes for x in range(no_of_nodes)]
    parent = [-1 for x in range(no_of_nodes)]

    visited[source] = VISITED
    all_nodes_visited -= 1
    weights[source] = 0
    parent[source] = source

    row_vector = [-1, 1, 0, 0]
    col_vector = [0, 0, 1, -1]

    for i in range(4):
        x = start_pos[1] + row_vector[i]
        y = start_pos[0] + col_vector[i]

        if size > x > -1 and size > y > -1:
            idx = x * size + y
            cell = maze[x][y]
            if cell != con.OBSTACLE:
                weights[idx] = 1
                parent[idx] = source

    while all_nodes_visited != 0:
        u = get_min_node(visited, weights, no_of_nodes)
        visited[u] = VISITED
        all_nodes_visited -= 1

        for i in range(4):
            x = int(u / size) + row_vector[i]
            y = u % size + col_vector[i]

            if size > x > -1 and size > y > -1:
                v = x * size + y
                cell = maze[x][y]
                if cell != con.OBSTACLE:
                    if weights[u] + 1 < weights[v]:
                        weights[v] = weights[u] + 1
                        parent[v] = u

    path = get_path(parent, source, destination, size)
    return path
