# sudoku_solver


## Introduction

A python script that will take in a text file with an unsolved sudoku puzzle and output the instructions of how to solve the sudoku with images of the completed sudokus.


## Working document

** A python file 'test.py' will be used to test solution ideas. (removed)
Moved away from having separate working and testing filies and instead working with git branches

The input file is called 'input.txt' and holds the unsolved sudoku puzzle. A secondary input file 'input_2.txt' is used to make a partially solved puzzle gradually more difficult to create new solving algorithms.

The puzzle solving script is 'solver.py' and split into separate functions that address increasing numbers of missing values in a row, column or 3x3 slice (all summerised as array from now on).


How the program solves a sudoku puzzle:

The '__main__' program checks if the puzzle has been solved and has a maximum of 10 iterations before exiting in case a solution cannot be found. All the solving will be done using called functions, as follows.

1. def single_number():
    An array that has a single missing number is solved. The function determines if a single value is missing by checking to see if there is a single 0 in the array, calculates the missing value from a difference between the summation of 1-9 minus the array sum.

2. def double_number(): 



## Output

Two files will be output: a completed sudoku array for reference and a text file that describes each step of the solution.


## Final Product

The idea is to have a quick script which the numbers from a Sudoku board can be input and will be able to solve in stages and display the changes. Future work will look into a gui.