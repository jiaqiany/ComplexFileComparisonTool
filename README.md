# ComplexFileComparisonTool
###Introduction:
A file comparison tool in python 3 which is able to deal with multiple complex situation.

###Purpose:
Find mtached lines with two files as many as possible.

###Progress:

####V1.0 Basic file comparison 3/18/2021
- Compare two files with unlimited sizes
- The tool will find where to start comparing by finding the first matched part
- A 100-lines buffer will be used for comparison
- Count number of missing lines (will fail if much more lines are different)
- Count number of unmated lines
- Display how many lines are compared and total lines
#####Need to Improve:
- Algorithm in the buffer (more unmated parts are find in a buffer)
- Counter number of missing lines and unmated lines
