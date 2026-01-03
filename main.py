import random
import copy

from fastapi import FastAPI

app = FastAPI()


SIZE = 9
CELLS_AMOUNT = SIZE * SIZE
MIN_CLUES = 17
MAX_CLUES = 30
VALID_BOX_RANGE = range(3)

def generate():
    return [[0] * SIZE for _ in range(SIZE)]

def print_grid(grid):
    for i in range(SIZE):
        if i != 0 and i % 3 == 0:
            print("------+-------+------")
        for j in range(SIZE):
            val = grid[i][j]
            print(grid[i][j], end=" ") if val != 0 else print(".", end=" ")
            if j == 8:
                print(" ")
            elif (j + 1) % 3 == 0:
                print("|", end=" ")

def get_box_cells(box_row, box_col):
    if box_row not in VALID_BOX_RANGE or box_col not in VALID_BOX_RANGE:
        raise ValueError("Box rows and cells must be in a valid range (0-2)")
    col_start = box_col * 3
    row_start = box_row * 3
    box_cells = []
    for i in range(row_start, row_start + 3):
        for j in range (col_start, col_start  + 3):
            box_cells.append((i,j))
    return box_cells

def validate_row(grid, row, val):
    for j in range(SIZE):
        if grid[row][j] == val:
            return False
    return True

def validate_col(grid, col, val):
    for i in range(SIZE):
        if grid[i][col] == val:
            return False
    return True

def validate_box(grid, row, col, val):
    box_cells = get_box_cells(row // 3, col // 3)
    for r, c in box_cells:
        if grid[r][c] == val:
            return False
    return True

def can_place_clue(grid, row, col, val):
    return (
        validate_row(grid, row, val) 
        and validate_col(grid, col, val) 
        and validate_box(grid, row, col, val)
    )

def find_empty_cell(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return (i,j)
    return None

def fill(grid):
    empty = find_empty_cell(grid)
    if empty is None:
        return True # Sudoku is solved

    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)

    for num in nums:
        if can_place_clue(grid, row, col, num):
            grid[row][col] = num

            if fill(grid):
                return True

            grid[row][col] = 0  # backtrack
    return False  

def count_solutions(grid, limit=2):
    empty = find_empty_cell(grid)
    if empty is None:
        return 1

    row, col = empty
    count = 0
    nums = list(range(1, 10))
    random.shuffle(nums)

    for num in nums:
        if can_place_clue(grid, row, col, num):
            grid[row][col] = num
            count += count_solutions(grid, limit)
            grid[row][col] = 0  # backtrack

            if count >= limit:
                return count
    return count  

def remove_clues(grid):
    clues_amount = random.randint(MIN_CLUES, MAX_CLUES)
    removed = 0

    cells = get_cells()
    random.shuffle(cells)

    for row, col in cells:
        if grid[row][col] == 0:
            continue

        if CELLS_AMOUNT - removed <= clues_amount:
            break

        backup = grid[row][col]
        grid[row][col] = 0

        grid_copy = copy.deepcopy(grid)
        if count_solutions(grid_copy) != 1:
            grid[row][col] = backup
        else:
            removed += 1

def get_cells():
    cells = []
    for i in range(SIZE):
        for j in range(SIZE):
            cells.append((i,j))
    return cells

def main():
    # empty grid
    grid = generate()
    # fill grid
    fill(grid)
    # save solution
    solution = copy.deepcopy(grid)
    # get puzzle
    remove_clues(grid)
    puzzle = grid

@app.get("/sudoku")
def generate_sudoku():
    grid = generate()
    fill(grid)

    solution = copy.deepcopy(grid)

    remove_clues(grid)
    puzzle = grid

    return {
        "puzzle": puzzle,
        "solution": solution
    }

