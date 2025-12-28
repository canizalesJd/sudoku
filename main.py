import random

SIZE = 9
MIN_CLUES = 2 # Minimum of clues per box (To make it unique must have 17+ clues)
MAX_CLUES = 4 # Max clues per box
VALID_BOX_RANGE = range(3)

def get_random(min_num, max_num):
    return random.randint(min_num, max_num)

def generate_grid():
    grid = []
    for _ in range(SIZE):
        box = []
        for _ in range(SIZE):
            box.append(0)
        grid.append(box)
    return grid

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

def place_box_clues(grid, box_cells):
    clues_amount = random.randint(MIN_CLUES, MAX_CLUES)

    random.shuffle(box_cells)
    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for row, col in box_cells[:clues_amount]:
        for clue in numbers:
            if can_place_clue(grid, row, col, clue):
                grid[row][col] = clue
                break
    return grid

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

def fill_grid(grid):
    for i in range(3):
        for j in range(3):
            box = get_box_cells(i,j)
            place_box_clues(grid, box)
    return grid


def main():
    grid = generate_grid()
    print_grid(fill_grid(grid))   


if __name__ == "__main__":
    main()
