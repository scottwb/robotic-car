# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def in_list(list, cell):
    for c in list:
        if ((c[1] == cell[1]) and (c[2] == cell[2])):
            return True
    return False

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

    expanded = []
    open     = [[0, init[0], init[1]]]

    #print "initial open list:"
    #for cell in open:
    #    print "    ", cell

    while (len(open) > 0):
        # Find the cell in open list with lowest g-value, remove it from
        # the open list, and add it to the expanded list.
        next_to_expand = None
        for cell in open:
            if ((next_to_expand == None) or (cell[0] < next_to_expand[0])):
                next_to_expand = cell
        open.remove(next_to_expand)
        expanded.append(next_to_expand)
        #print "----"
        #print "take list item"
        #print next_to_expand

        # Check to see if the chosen list item is the goal.
        if ((next_to_expand[1] == goal[0]) and
            (next_to_expand[2] == goal[1])):
            #print "###### Search successful"
            return next_to_expand
        
        # Expand the chosen cell by finding all its neighbors that:
        #   * aren't already in the expanded list
        #   * aren't already in the open list
        #   * aren't blocked
        #   * aren't out of bounds
        # and adding those to the open list
        for dir in delta:
            cell = [next_to_expand[0] + cost,
                    next_to_expand[1] + dir[0],
                    next_to_expand[2] + dir[1]]
            if ((cell[1] >= 0) and (cell[1] < len(grid))     and
                (cell[2] >= 0) and (cell[2] < len(grid[0]))  and
                (grid[cell[1]][cell[2]] == 0)                and
                not in_list(open, cell)                      and
                not in_list(expanded, cell)):
                open.append(cell)

        #print "new open list:"
        #for cell in open:
        #    print "    ", cell

    # If we get here, we ran out of cells to expand without ever
    # finding the goal.
    return "fail"


#------------------------------
print search()



