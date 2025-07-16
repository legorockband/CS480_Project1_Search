"""
This file will contain all of the algos for the vacuum world cleaning 
To run the file it will be in the format of:
    -python3 planner.py [search algo] [.txt file]

Examine the command line arguments and run either uniform cost or DFS on the text file provided.

"""

import sys
import time

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
    grid, grid_rows, grid_cols = text_parsing(input_text_file)

    ## Find the important aspects of the grid and create a list of the 
    start_position, dirty_cells, blocked_cells = find_important_cells(grid)

    print(dirty_cells)

    ## Create an empty 2D array of the visited cells 
    visited_cells = [[False for _ in range(grid_cols)] for _ in range(grid_rows)]

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
Args:
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

    return world_grid, rows, columns

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

Args:
- grid_rows = The total number of rows in the grid 
- grid_cols = The total number of columns in the grid
- bot_pos = The row and column that the robot is in 
- blocked_cells = These are all of the positions that contain a '#'
- visited_cells = The list of all of the cells that have already been visited in the grid

Output: 
- visited_cells: This will have an updated list of the cells that have been visited 
"""
def valid_cell(grid_rows, grid_cols, bot_pos, blocked_cells, visited_cells):
    x_pos, y_pos = bot_pos
    
    ## Check if the bot is going to move off of the grid
    if(x_pos >= grid_rows or y_pos >= grid_cols or x_pos < 0 or y_pos < 0):
        return False

    ## Check if the node has been visited already
    if(visited_cells[x_pos][y_pos]):
        return False

    ## Check if any bot is going to be on any of the blocked cells
    if(bot_pos in blocked_cells):
        return False

    ## This means that the cell is valid and can be moved to
    return True

def depth_first(grid, pos, visited_cells, blocked_cells, dirty_cells, direction_moved="Start", cleaned_cells=set(), complete_cleaning=[False]):
    ## Once the cleaning is done, exit out of the search
    if complete_cleaning[0]:
        return
    
    time.sleep(0.1)

    ## Current position of the bot on the grid 
    current_row, current_col = pos

    ## Check if we have visited the current node, if the node is blocked, or if we are out of bounds
    if not valid_cell(len(grid), len(grid[0]), pos, blocked_cells, visited_cells):
        return 

    ## Add the current position to the visited cell list
    visited_cells[current_row][current_col] = True

    print(f"Current visiting cell {pos}")

    ## Check if the current cell has a dirty spot
    if grid[current_row][current_col] == '*':
        cleaned_cells.add(pos)
        print(f"Cleaned")

    ## Check if all of the dirty cells have been cleaned
    if(cleaned_cells == dirty_cells):
        print("All dirty cells are clean")
        complete_cleaning[0] = True
        return 

    ## Move left, right, up, down 
    depth_first(grid, (current_row, current_col - 1), visited_cells, blocked_cells, dirty_cells, direction_moved="W", cleaned_cells=cleaned_cells, complete_cleaning=complete_cleaning)  ## Left movement
    depth_first(grid, (current_row, current_col + 1), visited_cells, blocked_cells, dirty_cells, direction_moved="E", cleaned_cells=cleaned_cells, complete_cleaning=complete_cleaning)  ## Right movement
    depth_first(grid, (current_row + 1, current_col), visited_cells, blocked_cells, dirty_cells, direction_moved="S", cleaned_cells=cleaned_cells, complete_cleaning=complete_cleaning)  ## Down movement
    depth_first(grid, (current_row - 1, current_col), visited_cells, blocked_cells, dirty_cells, direction_moved="N", cleaned_cells=cleaned_cells, complete_cleaning=complete_cleaning)  ## Up movement

def uniform_cost(grid, rows, columns):


    return 0



if __name__ == "__main__":
    main()