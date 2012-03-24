# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000.0 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0.0:
                        value[x][y] = 0.0
                        policy[x][y] = '*'
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        # The action taken if we fail to the left or right
                        a_left = (a + 1) % len(delta)
                        a_right = (a - 1) % len(delta)

                        # The cell we end up in if successful in this dir
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        # Cell we end up in if we fail to the left
                        x_left = x + delta[a_left][0]
                        y_left = y + delta[a_left][1]

                        # Cell we end up in if we fail to the right
                        x_right = x + delta[a_right][0]
                        y_right = y + delta[a_right][1]

                        # v2: value from probabilty of going this dir
                        if ((x2 >= 0) and (x2 < len(grid)) and
                            (y2 >= 0) and (y2 < len(grid[0])) and
                            (grid[x2][y2] == 0)):
                            v2 = value[x2][y2]
                        else:
                            v2 = float(collision_cost)
                        v2 = v2 * success_prob

                        # v_left: value from probability of failing left
                        if ((x_left >= 0) and (x_left < len(grid)) and
                            (y_left >= 0) and (y_left < len(grid[0])) and
                            (grid[x_left][y_left] == 0)):
                            v_left = value[x_left][y_left]
                        else:
                            v_left = float(collision_cost)
                        v_left = v_left * failure_prob

                        # v_right: value from probability of failing right
                        if ((x_right >= 0) and (x_right < len(grid)) and
                            (y_right >= 0) and (y_right < len(grid[0])) and
                            (grid[x_right][y_right] == 0)):
                            v_right = value[x_right][y_right]
                        else:
                            v_right = float(collision_cost)
                        v_right = v_right * failure_prob

                        # v_new: value of going this dir (a) from this cell
                        v_new = v2 + v_left + v_right + float(cost_step)

                        # Update the value of this cell if the value of
                        # going this direction is less than what we've
                        # computed before
                        if v_new < value[x][y]:
                            change = True
                            value[x][y] = v_new
                            policy[x][y] = delta_name[a]

    #for row in value:
    #    print row
    #for row in policy:
    #    print row

    return value, policy

#stochastic_value()

