# Sudoku_rev03.py - Sudoku Problem solver
#

#  20200730 - Successfully check and solving if a row has a single zero in rev02
#               rev03 will expand to colmn check logic
#  20200729 - New revisoin because the code was working and I don't want
#             to mess that up when I introduce a do while true loop
#  20200726 - Renamed this because I messed this up beyond recovery.
#  20200725 - started converting to functions - code not working with pushed
#  20200720 - I moved the code out of the 100DaysOfCode.  It will be easier to
#             track it this way.  Converted input to numpy
##
#
################################################################################
#
#  Needed to open the input file
import os
#  Used to process the input file
import pandas
#  To work with arrays
import numpy as np
#-------------------------------------------------------------------------------
def missing_number(zeros_removed):
    for missing in range(1, 10):
        if missing in zeros_removed:
            print(missing," is on the list")
        else:
#            print(missing, "is the missing number")
#            x = missing
            return missing

def check_row(row_y):
    get_row = sudoku_9x9_in[row_y]
    print("Row Y=",row_y," = ",get_row)
    sort_row = np.sort(get_row)
#    print(sort_row)
    zeros_removed = sort_row[sort_row > 0]
#    print("In the loop")
    return zeros_removed


#-------------------------------------------------------------------------------
#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')
#print(sudoku_9x9_in)

point_x = 0
point_y = 0

while True:
    #  Read from top right to bottom left
    #while point_x < 9:
    #while point_x in range(0,9):
        point = sudoku_9x9_in[point_y,point_x]
        print("Y=",point_y," X",point_x," value = ",point)
        if  point == 0:
    #        print(point," We found a zero!")
    #        print("zero Found - Location:  Y=",point_y," X=",point_x)
            zeros_removed = check_row(point_y)
    #        print(zeros_removed)
            if len(zeros_removed) == 8:
                print("Single Zero Found:  Y=",point_y," X=",point_x)
                x = missing_number(zeros_removed)
    #            print("Returned missing number is ",x)
    #            print(sudoku_9x9_in[point_y,point_x])
                sudoku_9x9_in[point_y,point_x] = x
    #            print(sudoku_9x9_in[point_y,point_x])
    #        break
                print("End of solve:",x,"at Y=",point_y," X=",point_x)
                print("The answer:")
                print(sudoku_9x9_in)
                point_y += 1
                point_x = 0
                continue   #forces restart of loop
            else:
                print("Multiple zeros next row")
                point_y += 1
                point_x = 0
                continue
        #    else:
    #        print(point," was found Y=",point_y," X",point_x)
        point_x += 1
        if point_x == 9:
            point_x = 0
            point_y += 1
            if point_y == 9:
                break
    #    print("Y=",point_y," X=",point_x," at While end")



#row_list = remove_0_from_row
#print(row_list)

#print(len(row_list))
#if len(row_list) == 8:
#    x = missing_number(row_list)
#    print("Returned missing number is ",x)


#print(check_3x3)


print("The answer:")
print(sudoku_9x9_in)
