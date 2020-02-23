#!/usr/bin/env python
import numpy as np


# Reading in sudoku array
sudoku_in = np.loadtxt("input.txt",dtype="int") # Reading in sudoku text file as numpy array
sudoku = sudoku_in
default = np.array([1,2,3,4,5,6,7,8,9]) # 1D array of sudoku numbers 




# Output
#print(sudoku_in)