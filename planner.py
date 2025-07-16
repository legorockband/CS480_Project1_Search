"""
This file will contain all of the algos for the vacuum world cleaning 
To run the file it will be in the format of:
    -python3 planner.py [search algo] [.txt file]

Examine the command line arguments and run either uniform cost or DFS on the text file provided.

"""

import sys

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

    start_position, dirty_cells = find_important_cells(grid)

    ## Check what algorithm you want to use 
    if (algo_to_run == "uniform_cost"):
        #uniform_cost(grid, start_position)
        return 0
    
    elif (algo_to_run == "depth_first"):
        depth_first(grid, start_position)
        return 0

    print(f"Usage: Wrong alogithm ran [{algo_to_run}], should be either uniform_cost or depth_first")

    return 0

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

    return world_grid

def find_important_cells(grid):
    dirty_cells = []
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            ## Find the start cell
            if grid[row][col] == '@':
                starting_pos = (row,col)
            
            ## Find dirty cell 
            elif grid[row][col] == '*':
                dirty_cells.append((row,col))

    return starting_pos, dirty_cells


def depth_first(grid, starting_pos):
    row = starting_pos[0]
    col = starting_pos[1]

    ## Create a stack with the starting position in there
    stack = [starting_pos]

    


    return 0

def uniform_cost(grid, rows, columns):


    return 0



if __name__ == "__main__":
    main()