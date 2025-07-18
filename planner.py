"""
This file will contain all of the algos for the vacuum world cleaning 
To run the file it will be in the format of:
    -python3 planner.py [search algo] [.txt file]

Examine the command line arguments and run either uniform cost or DFS on the text file provided.

"""

import sys
import copy

## (<direction>, <row>, <column>)
direction_vector = [
    ("W", 0, -1), 
    ("E", 0,  1),
    ("N", -1, 0),
    ("S", 1 , 0)
]

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 planner.py [search algorithm] [.txt file]")
        sys.exit(1)

    algo_to_run = sys.argv[1]

    if sys.argv[2].endswith(".txt"):
        input_text_file = sys.argv[2]
    
    else:
        print(f"Usage: Make sure [{sys.argv[2]}] is in .txt format")
        sys.exit(1)

    ## Create Grid from txt file
    grid = text_parsing(input_text_file)

    ## Find the important aspects of the grid and create a list of the 
    start_position, dirty_cells, blocked_cells = find_important_cells(grid)

    ## Create an empty 2D array of the visited cells 
    visited_cells = set()

    ## Check what algorithm you want to use 
    if (algo_to_run == "uniform_cost"):
        #uniform_cost(grid, start_position)
        return 
    
    elif (algo_to_run == "depth_first"):
        depth_first(grid, start_position, visited_cells, blocked_cells, dirty_cells)
        return 

    print(f"Usage: Wrong alogithm ran [{algo_to_run}], should be either uniform_cost or depth_first")

    return 

"""
Parameter:
  -text_file: The input file from the command line argument

Output:
  -2D array of empty, blocked, dirty, and starting cells 
    - `_` for empty
    - `#` for blocked
    - `*` for dirty
    - `@` for robot start (placed randomly in a non-blocked, non-dirty cell)
  - Starting row and column 
"""
def text_parsing(text_file):
    with open(text_file, 'r', encoding='utf-16') as file:
        columns = int(file.readline().strip())
        rows = int(file.readline().strip())

        world_grid = []

        ## Go through each line in a row and add it to a list
        for _ in range(rows):
            grid_line = file.readline().strip()
            world_grid.append(grid_line)
            
    file.close()

    return world_grid

def find_important_cells(grid):
    dirty_cells = set()
    blocked_cells = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            ## Find the start cell
            if grid[row][col] == '@':
                starting_pos = (row,col)
            
            ## Find dirty cell 
            elif grid[row][col] == '*':
                dirty_cells.add((row,col))

            ## Find the blocked cells
            elif grid[row][col] == '#':
                blocked_cells.add((row, col))
            
    return starting_pos, dirty_cells, blocked_cells

"""
Function that checks to make sure the vacuum can move to that cell or hasn't already been to that cell

Parameter:
- grid_rows = The total number of rows in the grid 
- grid_cols = The total number of columns in the grid
- bot_pos = The row and column that the robot is in 
- blocked_cells = These are all of the positions that contain a '#'
- visited_cells = The list of all of the cells that have already been visited in the grid

Output: 
- visited_cells: This will have an updated list of the cells that have been visited 
"""
def valid_cell(grid, bot_pos, blocked_cells, visited_cells):
    x_pos, y_pos = bot_pos
    
    ## Check if the bot is going to move off of the grid
    if(x_pos >= len(grid) or y_pos >= len(grid[0]) or x_pos < 0 or y_pos < 0):
        return False

    ## Check if the node has been visited already
    if(bot_pos in visited_cells):
        return False

    ## Check if the bot position is going to be on any of the blocked cells
    if(bot_pos in blocked_cells):
        return False

    ## This means that the cell is valid and can be moved to
    return True

"""
Parameters: 
- grid [[]]: A 2D array that holds the vacuum world inside it 
- pos (int, int): A tuple that holds the position for the robot
- visited_cells [[]]: Holds a boolean on whether or not the robot has visited a cell
- blocked_cells [(int, int)]: A list that holds all of the cell positions that are blocked
- dirty_cells [(int, int)]: A list of all the dirty cells on the grid
- direction_moved (string): Direction that the robot has moved 
- cleaned_cells [(int, int)]: A list of all the dirty cells that have been cleaned already
- complete_cleaning (bool): Flag to keep track of when all the cells have been cleaned to stop excessive recursions 
- nodes_expanded (int): Number of nodes that get have there children searched through
- nodes_generated (int): Number of nodes that get traversed
- path []: The path from the robot to a dirty cell
- final_path [[]]: The path for the robot to get to every single dirty cell
- direction_log []: Track all of the directions that the robot went to make it to a dirty cell

Output:
- stdout print statments 
  1. Directions the robot took 
  2. <nodes_generated> nodes generated
  3. <nodes_expanded> nodes expanded

"""
def depth_first(grid, pos, visited_cells, blocked_cells, dirty_cells, direction_moved="Start", 
                cleaned_cells=None, complete_cleaning=None, nodes_expanded=None, nodes_generated=None,
                path=None, final_path=None, direction_log=None):
    
    if cleaned_cells is None: cleaned_cells = set()
    if complete_cleaning is None: complete_cleaning = [False]
    if nodes_expanded is None: nodes_expanded = [0]
    if nodes_generated is None: nodes_generated = [0]
    if path is None: path = []
    if final_path is None: final_path =[[]]
    if direction_log is None: direction_log = []

    ## Once the cleaning is done, exit out of the search
    if complete_cleaning[0]: return

    ## Current position of the bot on the grid 
    current_row, current_col = pos

    nodes_generated[0] += 1

    ## Check if we have visited the current node, if the node is blocked, or if we are out of bounds
    if not valid_cell(grid, pos, blocked_cells, visited_cells): return 

    ## Add the current position to the visited cell list
    visited_cells.add(pos)
    nodes_expanded[0] += 1
    path.append(pos)
 
    if(direction_moved != "Start"):
        direction_log.append(direction_moved)

    ## Check if the current cell has a dirty spot
    if grid[current_row][current_col] == '*' and pos not in cleaned_cells:
        cleaned_cells.add(pos)
        direction_log.append("V")

    ## Check if all of the dirty cells have been cleaned
    if(cleaned_cells == dirty_cells):
        complete_cleaning[0] = True
        final_path[0] = path.copy()
        for movement in direction_log:
            print(movement)
        print(f"{nodes_generated[0]} nodes generated")
        print(f"{nodes_expanded[0]} nodes expanded")
        return 
    
    ## Move left, right, up, down
    for moved, dir_r, dir_c in direction_vector:
        next_pos = (current_row + dir_r, current_col + dir_c)
        depth_first(grid, next_pos, visited_cells=visited_cells.copy(), blocked_cells=blocked_cells, dirty_cells=dirty_cells,
                    direction_moved=moved,cleaned_cells=cleaned_cells.copy(), complete_cleaning=complete_cleaning, 
                    nodes_expanded=nodes_expanded, nodes_generated=nodes_generated,path=path.copy(), final_path=final_path, direction_log=direction_log.copy())

def uniform_cost(grid, rows, columns):

    
    return 0


if __name__ == "__main__":
    main()