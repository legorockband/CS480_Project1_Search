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

    grid = text_parsing(input_text_file)

    if (algo_to_run == "uniform_cost"):
        uniform_cost()
        return 0
    
    elif (algo_to_run == "depth_first"):
        depth_first()
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
"""

def text_parsing(text_file):
    with open(text_file, 'r', encoding='utf-16') as file:
        columns = int(file.readline().strip())
        rows = int(file.readline().strip())

        world_grid = []
        for _ in range(rows):
            grid_line = file.readline().strip()
            world_grid.append(grid_line)
    file.close()

    return world_grid


def uniform_cost():


    return 0

def depth_first():





    return 0

if __name__ == "__main__":
    main()