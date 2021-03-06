# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]


    #### ENTER CODE BELOW THIS LINE ###
    change = True
    while change:
        change = False
        for i in range(len(path)):
            if ((i == 0) or (i == (len(path)-1))):
                # Skip first and last point
                continue
            for j in range(len(path[0])):
                xi      = float(path[i][j])
                yi      = float(newpath[i][j])
                yi_prev = float(newpath[i-1][j])
                yi_next = float(newpath[i+1][j])

                # Using serial update
                yi += float(weight_data) * (xi - yi)
                yi += float(weight_smooth) * (yi_next + yi_prev - (2 * yi))

                # Using simultaneous update
                #alpha = float(weight_data) * (xi - yi)
                #beta = float(weight_smooth) * (yi_next + yi_prev - (2 * yi))
                #yi += (alpha + beta)

                if abs(newpath[i][j] - yi) > 0.000001:
                    change = True
                    newpath[i][j] = yi
    
    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'





