# Sudoku_rev00.py - Sudoku Problem solver
#
#  20200720 - I moved the code out of the 100DaysOfCode.  It will be easier to
#             track it this way.  Converted input to numpy
#
################################################################################
#
#  Needed to open the input file
import os
#  Used to process the input file
import pandas
#  To work with arrays
import numpy as np

#  Read the puzzle - 0 is missing number
#if os.path.exists("9x9_in.csv"):
#    input_9x9_df = pandas.read_csv("9x9_in.csv", header=None)
#    print(input_9x9_df)
#    print('----------------------------------------')
#else:
#    print("file does not exist")
#  Iterate through the upper right 3x3
#     Note:  does not read the last value

#  Create a numpy array filled with zeros
#sudoku_row=np.zeros(9)
#sudoku_col=np.zeros(9)

#print(sudoku_row)
#print(sudoku_col)

#  This build an array fille with zeros in the shape of 9x9
#sudoku_9x9=np.zeros([(9),(9)])
#print("Array Shape = ",sudoku_9x9.shape)

#print(sudoku_9x9)
#
#  Build the cube
#sudoku_cube=np.ones([(9),(9),(5)])
#print("Array Shape = ",sudoku_cube.shape)

#print(sudoku_cube)

#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')
print(sudoku_9x9_in)

box_x_start = 0
box_x_end = box_x_start + 3
box_y_start = 0
box_y_end = box_x_start + 3
check_3x3 = sudoku_9x9_in[box_y_start:box_y_end,box_x_start:box_x_end]
print(check_3x3)

check_3x3 > 0

line_3x3 = np.reshape(check_3x3,(1,9))
sort_line = np.sort(line_3x3)
print(sort_line)

print(check_3x3)



#print(sudoku_9x9_in > 0)
