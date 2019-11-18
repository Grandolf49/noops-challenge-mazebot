# Libraries
import maze_api_handler as maze_api
import constants as con
import maze_solver as solve

# Get the puzzle
maze_data_json = maze_api.get_random_maze()
print(maze_data_json)

# Initialize some variables
maze_path = maze_data_json[con.STR_MAZE_PATH]
maze = maze_data_json[con.STR_MAP]
start_pos = maze_data_json[con.STR_START_POS]
end_pos = maze_data_json[con.STR_END_POS]

# Get solution to the maze
answer = solve.solve_maze(maze, start_pos, end_pos)

# Post this solution to API
response = maze_api.post_result_directions(answer, maze_path)

print(response)
