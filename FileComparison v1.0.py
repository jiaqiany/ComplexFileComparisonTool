# Python 3

import sys
import re

# check if file2 starts first
file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "r")
line1 = file1.readline()
line2 = file2.readline()

flag = 0
matchedLines = 0 # if lines in two files are fully matched
unmatched = 0 # if lines are not matched compared with two files 

if lineLog1 in file2:
    while True:
        line2 = file2.readline()
        line1 = file1.readline()
        # compare passed if every lines of either file are checked 
        if not line1 or not line2:
            break
        
        if line1 != line2:
            flag += 1 # the test is failed already
            searchList = [] 
            for i in range(0,100):
                searchList.append(line2)
                line2 = file2.readline()
            while line1 not in searchList: 
                unmatched += 1 
                line1 = file1.readline()
            while line1 in searchList:
                matchedLines += 1
                line1 = file1.readline() 
            if line1 != line2:
                break

        if line1 == line2:
            matchedLines += 1


# Thus file1 will start first
secondFile1 = open(sys.argv[1], "r")
secondFile2 = open(sys.argv[2], "r")
secondLine1 = secondFile1.readline()
secondLine2 = secondFile2.readline()

if secondLine2 in secondFile1:
    while True:
        secondLine2 = secondFile2.readline()
        secondLine1 = secondFile1.readline()
        # compare passed if every lines of either file are checked 
        if not secondLine or not secondLine2:
            break
        
        if secondLine2 != secondLine1:
            flag += 1 # the test is failed already
            searchList = [] # a 100 lines buffer for searching lines
            for i in range(0,100):
                searchList.append(secondLine1)
                secondLine1 = secondFile1.readline()
                # pointer of file2 is located on the next line out of buffer
            while secondLine2 not in searchList:
                # count for both lost lines and different lines
                unmatched += 1
                secondLine2 = secondFile2.readline()
            while secondLine2 in searchList:
                matchedLines += 1
                secondLine2 = secondFile2.readline()
            # end when all the rest lines in the buffer are matched
            # the pointers on both file1 and file2 should be matched at this point
            # if there are more unmated lines, compare will fail
            if secondLine1 != secondLine2:
                break

        if secondLine1 == secondLine2:
            matchedLines += 1

if flag == 0:
    print("Compare passed!")
else:
    print("Compare failed...")
    print("%(unmatched)d lines are unmatched." % {"unmatched": unmatched})
    print("%(matchedLines)d lines are matched." % {"matchedLines": matchedLines})
