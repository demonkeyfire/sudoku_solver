#!/usr/bin/env python
import numpy as np


# Reading in sudoku array
sudoku_in = np.loadtxt("input.txt",dtype="int") # Reading in sudoku text file as numpy array
sudoku = sudoku_in # Backing up input sudoku
default = np.array([1,2,3,4,5,6,7,8,9]) # 1D array of sudoku numbers


#while (np.any(sudoku==0))==True: # Checking if the sudoku is solved

# Searching rows for single missing values
for i in range(0,9): # cycling through all rows
    line = sudoku_in[i,:] # picking up each row
    if (np.sum(np.isin(line,default))) == 8: # checking if a single value is missing
        number = 45 - np.sum(line) # calculating missing value
        location = np.argwhere(line==0) # location of missing value
        line = np.where(line==0, number, line) # replacing missing value 

# Searching columns for single missing values
for i in range(0,9):
    line = sudoku_in[:,i]
    if (np.sum(np.isin(line,default))) == 8:
        number = 45 - np.sum(line)
        location = np.argwhere(line==0)
        line_new = np.where(line==0, number, line)

# Searching the 3x3 arrays for single solutions
slices = {}
for i in range(0,3):
    for j in range(0,3):
        slices["slice_"+str(i)+"_"+str(j)] = sudoku_in[j*3:(j*3)+3,i*3:(i*3)+3]
        if (np.sum(np.isin(slices["slice_"+str(i)+"_"+str(j)],default))) == 8:
            number = 45 - np.sum(slices["slice_"+str(i)+"_"+str(j)])
            location = np.argwhere(slices["slice_"+str(i)+"_"+str(j)]==0)
            slices["slice_new_"+str(i)+"_"+str(j)] = np.where(slices["slice_"+str(i)+"_"+str(j)]==0, number, slices["slice_"+str(i)+"_"+str(j)])



# Output
#print(sudoku_in)