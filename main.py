# Libraries
import maze_api_handler as maze_api
import constants as con
import maze_solver as solve

# Get a random maze puzzle
maze_data_json = maze_api.get_random_maze()
print(maze_data_json)

# Initialize some variables
maze_path = maze_data_json[con.STR_MAZE_PATH]
maze = maze_data_json[con.STR_MAP]
start_pos = maze_data_json[con.STR_START_POS]
end_pos = maze_data_json[con.STR_END_POS]

# Get solution to the maze
'''
maze = [
    ['X', ' ', ' ', ' ', ' '],
    [' ', ' ', 'X', ' ', ' '],
    [' ', 'A', ' ', 'X', 'X'],
    [' ', 'X', 'X', 'X', 'B'],
    [' ', ' ', ' ', ' ', ' ']
]
start_pos = [1, 2]
end_pos = [4, 3]
'''

# answer_bfs = solve.solve_maze_bfs(maze, start_pos, end_pos)
answer = solve.solve_maze_dijkstraj(maze, start_pos, end_pos)
print(answer)

# Post this solution to API
response = maze_api.post_result_directions(answer, maze_path)

print(response)

'''
# Get race puzzle
puz = maze_api.post_start_race('Grandolf49')

while True:
    # print('New Puzzle')
    next_maze = puz[con.STR_NEXT_MAZE]
    maze_data_json = maze_api.get_maze_race_mode(next_maze)
    # print(maze_data_json)

    maze = maze_data_json[con.STR_MAP]
    maze_path = maze_data_json[con.STR_MAZE_PATH]
    start_pos = maze_data_json[con.STR_START_POS]
    end_pos = maze_data_json[con.STR_END_POS]

    # Get solution to the maze
    # print('Getting Solution')
    answer = solve.solve_maze(maze, start_pos, end_pos)

    # Post this solution to API
    # print('Sending Solution')
    puz = maze_api.post_result_directions(answer, maze_path)
    if puz[con.STR_RESULT] == con.STR_FINISHED:
        print(maze_data_json)
        print(puz)
        break

'''
