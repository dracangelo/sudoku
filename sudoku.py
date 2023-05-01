def is_valid_moves(grid, row, col, number):

    for x in range(9):
        if grid[row][x] == number:
            return False # row
    
    for x in range(9):
        if grid[x][col] == number:
            return False # col
        
    corner_row = row - row %  3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False # corner
        
    return True # valid moves

def solve(grid, row, col):

    if col == 9:
        if row == 8:
            return True 
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1) 
    
    for num in range(1, 10): #123456789

        if is_valid_moves(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True
            
            grid[row][col] = 0

            return False
        
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
] #insert your grid here

if solve(grid, 0, 0):
        for i in range(9):
            for j in range (9):
                print(grid[i][j], end=" ")
                print()
else:
        print("no solution for this sudoku")