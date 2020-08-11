# Sudoku_rev08.py - Sudoku Problem solver
#
#  20200810 - Starting Rev08 - The logic is not "forward thinking" enough to
#               select the correc answer in all cases.  Switching from solving
#               as while stpping through the puzzle I will read the puzzle
#               and look for "low hanging fruit"
#
################################################################################
#
#  Needed to open the input file
import os
# Used to process the input file
import pandas
#  To work with arrays
import numpy as np

import collections, numpy
#-------------------------------------------------------------------------------
#convert a 3x3 box to a list
def check_3x3(point_y,point_x):
    if point_y < 3:
        box_y_start = 0
        box_y_end = 3
    elif point_y < 6:
        box_y_start = 3
        box_y_end = 6
    else:
        box_y_start = 6
        box_y_end = 9
    if point_x < 3:
        box_x_start = 0
        box_x_end = 3
    elif point_x < 6:
        box_x_start = 3
        box_x_end = 6
    else:
        box_x_start = 6
        box_x_end = 9
    box_3x3 = sudoku_9x9_in[box_y_start:box_y_end,box_x_start:box_x_end]
    return box_3x3

def number_count():
    number_hold = 0
    for i in range (1, 10):
        number_check = np.count_nonzero(sudoku_9x9_in == i)
#        print("count ",i," = ",np.count_nonzero(sudoku_9x9_in == i))
        print("Count ",i," = ",number_check)
#        print("Number Hold = ",number_hold)
        if number_check > number_hold and number_check < 9:
            george = i
            number_hold = number_check
#            print("Solve for = ",george)
    return george

#-------------------------------------------------------------------------------
#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')

z = 0
point_x = 3
point_y = 1
zero_hold = 0
solve_number = number_count()
print("Solve for = ",solve_number)

check_cell = sudoku_9x9_in[point_y,point_x]
print("Check Cell = ",check_cell)
check_row = sudoku_9x9_in[point_y]
print("Row Y=",point_y," is ",check_row)
check_column = sudoku_9x9_in[:,point_x]
print("Col X=",point_x," is ",check_column)
check_box = check_3x3(point_y,point_x)
print(check_box)

all_numbers = numpy.array(check_row)
all_numbers = numpy.append(all_numbers,check_column)
print("All Numbers = ",all_numbers)
line_3x3 = np.reshape(check_box,(1,9))
all_numbers = numpy.append(all_numbers,line_3x3)
print("All Numbers = ",all_numbers)
nonzero_numbers = all_numbers[all_numbers > 0]
print("Non-zero Numbers = ",nonzero_numbers)
sorted_numbers = np.sort(nonzero_numbers)
#sort_line = np.sort(line_3x3)
#    print(sort_line)
print("Sorted Numbers = ",sorted_numbers)
unique_numbers = np.unique(sorted_numbers)
print("Unique Numbers = ",unique_numbers)

solve_numbers = 0

for i in range (1, 10):
    #print("i = ",i)
    if i in unique_numbers:
        z += 1
    else:
        solve_numbers = numpy.append(solve_numbers,i)
        #print("Solve Numbers = ",solve_numbers)

print("Solve Numbers = ",solve_numbers)
non_zero_solve_numbers = solve_numbers[solve_numbers > 0]
print("Non Zero Solve Numbers = ",non_zero_solve_numbers)
possible_count = non_zero_solve_numbers.size
print("Possible Count = ",possible_count)



possible_array=numpy.array([point_y])
possible_array = numpy.append(possible_array,[point_x])
possible_array = numpy.append(possible_array,possible_count)
possible_array = numpy.append(possible_array,non_zero_solve_numbers)
print(possible_array)




#print("The Final Answer:")
#print(sudoku_9x9_in)
