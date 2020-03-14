#!/usr/bin/env python
import numpy as np


# Reading in sudoku array
sudoku_in = np.loadtxt("input.txt",dtype="int") # Reading in sudoku text file as numpy array
sudoku = sudoku_in # Backing up input sudoku
default = np.array([1,2,3,4,5,6,7,8,9]) # 1D array of sudoku numbers


# ------------------------DEFINING THE ROWS AND COLUMNS OF THE SUDOKU PUZZLE-----------------------

# A dictionary of the rows
rows = {}
for i in range(0,9): # cycling through all rows
    rows["row_" + str(i)] = sudoku_in[i,:] # picking up each row

# A dictionary of the columns
columns = {}
for i in range(0,9):
    columns["column_" + str(i)] = sudoku_in[:,i]

# Creating a dictionary of the slices
slices = {}
for i in range(0,3):
    for j in range(0,3):
        slices["slice_"+str(i)+"_"+str(j)] = sudoku_in[j*3:(j*3)+3,i*3:(i*3)+3]


# --------------------------------SOLVING FOR A SINGLE MISSING VALUE-------------------------------

def single_number():
    k = 0
    while (np.any(sudoku==0))==True: # Checking if the sudoku is solved
        k += 1
        if k > 10:
            exit()
        else:
            # Searching rows for single missing values
            if (np.sum(np.isin(rows["row_" + str(i)],default))) == 8: # checking if a single value is missing
                number = 45 - np.sum(rows["row_" + str(i)]) # calculating missing value
                location = np.argwhere(rows["row_" + str(i)]==0) # location of missing value
                rows["row_" + str(i)] = np.where(rows["row_" + str(i)]==0, number, rows["row_" + str(i)]) # replacing missing value

            # Searching columns for single missing values
            if (np.sum(np.isin(columns["column_" + str(i)],default))) == 8:
                number = 45 - np.sum(columns["column_" + str(i)])
                location = np.argwhere(columns["column_" + str(i)]==0)
                columns["column_" + str(i)] = np.where(columns["column_" + str(i)]==0, number, columns["column_" + str(i)])

            # Searching the 3x3 arrays for single solutions
            if (np.sum(np.isin(slices["slice_"+str(i)+"_"+str(j)],default))) == 8:
                number = 45 - np.sum(slices["slice_"+str(i)+"_"+str(j)])
                location = np.argwhere(slices["slice_"+str(i)+"_"+str(j)]==0)
                slices["slice_new_"+str(i)+"_"+str(j)] = np.where(slices["slice_"+str(i)+"_"+str(j)]==0, number, slices["slice_"+str(i)+"_"+str(j)])

                