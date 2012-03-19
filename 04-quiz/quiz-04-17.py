# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def propagate(value, x, y):
    v = value[x][y]
    to_propagate = []
    for d in delta:
        nx = x - d[0]
        ny = y - d[1]
        if ((nx >= 0) and (nx < len(grid))    and
            (ny >= 0) and (ny < len(grid[0])) and
            (grid[nx][ny] != 1)):
            existing_v = value[nx][ny]
            new_v = v + cost_step
            if new_v < existing_v:
                value[nx][ny] = new_v
                to_propagate.append([nx, ny])
    for cell in to_propagate:
        propagate(value, cell[0], cell[1])

def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = goal[0]
    y = goal[1]
    value[x][y] = 0
    propagate(value, x, y)

    for row in value:
        print row

    return value #make sure your function returns a grid of values as demonstrated in the previous video.


compute_value()
