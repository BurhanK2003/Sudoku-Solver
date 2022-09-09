#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sudoku solver
from pprint import pprint

def find_next_empty(puzzle):
    #any open spaces will be marked as -1
    #this function will find the empty spaces for us
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None, None # if no spaces in the puzzle are left

############################################################
# SOLVER IMPLEMENTATION
############################################################

def is_valid(puzzle, guess, row, col):
    #figures is the guess is valid or not
    #returns valid if true and false otherwiswe
    row_vals= puzzle[row]
    if guess in row_vals:
        return False
    #now the cols
    col_vals=[]
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    #and then the 3x3 squres 
    #we need to know where the 3x3 index starts and where and iterate over the 3 values in the rows/cols
    row_start = (row // 3)*3
    col_start = (col // 3)*3 
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    #if we get here then it is valid
    return True

            

def solve_sudoku(puzzle):
    row, col= find_next_empty(puzzle)
    # now we implement some validation checks
    if row == None:
        return True
    for guess in range (1,10):
        #check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # if the value is valid then we want to place the guess on the puzzle
            puzzle[row][col] = guess
            # recursively call our function
            if solve_sudoku(puzzle):
                return True
    #what if our guess doesn't solve the puzzle? We must backtrack and try again
        puzzle[row][col] = -1 #resets the guess
    
    #if every combination is tried and still not solved than this puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
        
    

