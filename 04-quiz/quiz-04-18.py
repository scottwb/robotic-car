# ----------
# User Instructions:
# 
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

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
# modify code below
# ----------------------------------------

def optimum_policy():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if goal[0] == x and goal[1] == y:
                policy[x][y] = '*'
            elif grid[x][y] == 0:
                actions = []
                for d in range(len(delta)):
                    nx = x + delta[d][0]
                    ny = y + delta[d][1]
                    if ((nx >= 0) and (nx < len(grid)) and
                        (ny >= 0) and (ny < len(grid[0])) and
                        (grid[nx][ny] == 0)):
                        actions.append([value[nx][ny], d])
                actions.sort()
                policy[x][y] = delta_name[actions[0][1]]

    for row in policy:
        print row
                                
    return policy # Make sure your function returns the expected grid.


optimum_policy()

# NOTE: I ran this on a bunch of examples and I am confident that it works
#       correctly and returns the same results as Sebastian's solution,
#       but for some reason, the Udacity server returns a 500 error every time
#       I try to submit it. I don't have time to debug this just for the hell
#       of it. I learned what I needed to learn and coded a working solution.
#       That's good enough for me right now.
