#!/usr/bin/env python
import numpy as np


# --------------------------------SOLVING FOR A SINGLE MISSING VALUE-------------------------------
def single_number(sudoku, default, k):
    # Searching rows for single missing values
    if k==0:
        for i in range(0,9):
            if (np.sum(np.isin(sudoku[i,:],default))) == 8: # checking if a single value is missing
                print("The initial row "+str(i+1)+":")
                print(sudoku[i,:])
                number = 45 - np.sum(sudoku[i,:]) # calculating missing value
                location = np.argwhere(sudoku[i,:]==0) # location of missing value
                sudoku[i,:] = np.where(sudoku[i,:]==0, number, sudoku[i,:]) # replacing missing value
                print("\nThe missing value at location "+str(np.asscalar(location)+1)+" is "+str(number))
                print("\nThe final row "+str(i+1) + ":")
                print(sudoku[i,:])
            result = sudoku
    elif k==1:
        for i in range(0,9):
            # Searching columns for single missing values
            if (np.sum(np.isin(sudoku[:,i],default))) == 8:
                print("The initial column "+str(i+1) + ":")
                print(sudoku[:,i])
                number = 45 - np.sum(sudoku[:,i])
                location = np.argwhere(sudoku[:,i]==0)
                sudoku[:,i] = np.where(sudoku[:,i]==0, number, sudoku[:,i])
                print("\nThe missing value at location "+str(np.asscalar(location)+1)+" is "+str(number))
                print("\nThe final column "+str(i+1)+":")
                print(sudoku[:,i])
            result = sudoku
    elif k==2:
        for i in range(0,3):
            for j in range(0,3):
            # Searching the 3x3 arrays for single solutions
                if (np.sum(np.isin(sudoku[j*3:(j*3)+3,i*3:(i*3)+3],default))) == 8:
                    print("The initial slice "+str(i+1)+","+str(j+1)+":")
                    print(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    number = 45 - np.sum(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    location = np.argwhere(sudoku[j*3:(j*3)+3,i*3:(i*3)+3]==0)
                    sudoku[j*3:(j*3)+3,i*3:(i*3)+3] = np.where(sudoku[j*3:(j*3)+3,i*3:(i*3)+3]==0, number, sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    print("\nThe missing value at location "+str(np.asscalar(location[0,0]))+","+str(np.asscalar(location[0,1]))+" is "+str(number))
                    print("\nThe initial slice "+str(i+1)+","+str(j+1)+":")
                    print(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                result = sudoku
    return result


# ----------------------------------SOLVING FOR TWO MISSING VALUES---------------------------------
def double_number(sudoku, default):
    # Finding the 0's in a row
    for i in range(0,9): # Searching through all columns
        if i==0: # Selecting first column (0)
            for j in np.setdiff1d(default,sudoku[:,i]): # cycling through missing numbers
                if j==1: # Selecting the missing number 1
                    for k in np.argwhere(sudoku[:,i]==0): # cycling through missing number column locations
                        if j in sudoku[k,:]: # Listing rows that have the number 1 in
                            print(sudoku[k,:])
                


# -------------------------------------------MAIN PROGRAM------------------------------------------
if __name__ == '__main__':

    sudoku_in = np.loadtxt("input_2.txt", dtype="int") # Reading in sudoku puzzle
    sudoku = sudoku_in # Backing up input sudoku to a working array
    default = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D array of sudoku numbers


    # Replace single values in rows, columns and slices
    '''count = 9
    while (np.any(sudoku==0))==True:
        count += 1
        if count > 10:
            exit()
        for i in range(0,3):
            single_number(sudoku, default, i)'''
    double_number(sudoku, default)