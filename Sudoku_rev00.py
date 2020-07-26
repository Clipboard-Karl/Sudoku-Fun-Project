# Sudoku_rev00.py - Sudoku Problem solver
#
#  20200725 - started converting to functions - code not working with pushed
#  20200720 - I moved the code out of the 100DaysOfCode.  It will be easier to
#             track it this way.  Converted input to numpy
#
#
################################################################################
#
#  Needed to open the input file
import os
#  Used to process the input file
import pandas
#  To work with arrays
import numpy as np

def missing_number(missing):
    for missing in range(1, 10):
        if missing in row_list:
            print(missing," is on the list")
        else:
            print(missing, "is the missing number")
#            x = missing
            return missing

#convert a 3x3 box to a list
def missing_3x3(box_x,box_y):
    box_x_start = box_x
    box_x_end = box_x_start + 3
    box_y_start = box_y
    box_y_end = box_x_start + 3
    check_3x3 = sudoku_9x9_in[box_y_start:box_y_end,box_x_start:box_x_end]
    print(check_3x3)
    check_3x3 > 0
    line_3x3 = np.reshape(check_3x3,(1,9))
    sort_line = np.sort(line_3x3)
    #print(sort_line)
    zeros_removed = sort_line[sort_line > 0]
    #print(zeros_removed)
    row_list = zeros_removed
    #print("Row list in function: ",row_list)
    return row_list


#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')
print(sudoku_9x9_in)


#  Convert a 3x3 box into a line

#row_list = missing_3x3(0,0)

#print("Row list as returned from function: ",row_list)



check_read = sudoku_9x9_in[0:1,0:9]
print(check_read)
sort_row = np.sort(check_read)
print(sort_row)
remove_0_from_row = sort_row[sort_row > 0]
print(remove_0_from_row)

#    line_3x3 = np.reshape(check_3x3,(1,9))
#    sort_line = np.sort(line_3x3)
#    #print(sort_line)
#    zeros_removed = sort_line[sort_line > 0]
#    #print(zeros_removed)
#    row_list = zeros_removed




row_list = remove_0_from_row

print(row_list)

#print(len(row_list))
if len(row_list) == 8:
    x = missing_number(row_list)
    print("Returned missing number is ",x)


#print(check_3x3)



#print(sudoku_9x9_in > 0)
