#!/usr/bin/env python

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

#----------MY CODE HERE ----------#

grid_height         = len(colors)
grid_width          = len(colors[0])
num_cells           = grid_width * grid_height
uniform_probability = 1.0 / num_cells

def init_distribution():
    distro = []
    for i in range(grid_height):
        row = []
        for j in range(grid_width):
            row.append(uniform_probability)
        distro.append(row)
    return distro

def sample(p, i, j):
    i = i % grid_height
    j = j % grid_width
    return p[i][j]

def sense(p, measurement):
    q_prime = []
    for i in range(grid_height):
        row = []
        for j in range(grid_width):
            if (measurement == colors[i][j]):
                row.append(sample(p,i,j) * sensor_right)
            else:
                row.append(sample(p,i,j) * (1.0 - sensor_right))
        q_prime.append(row)
    alpha = sum(map((lambda(r): sum(r)), q_prime))
    q = []
    for i in range(grid_height):
        row = []
        for j in range(grid_width):
            row.append(q_prime[i][j] / alpha)
        q.append(row)
    return q

def move(p, vector):
    delta_i = vector[0]
    delta_j = vector[1]
    q = []
    for i in range(grid_height):
        row = []
        for j in range(grid_width):
            p_moved       = sample(p, i - delta_i, j - delta_j) * p_move
            p_didnt_move = sample(p, i, j) * (1.0 - p_move)
            row.append(p_moved + p_didnt_move)
        q.append(row)
    return q

p = init_distribution()
for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])

#----------END MY CODE -----------#



#Your probability array must be printed 
#with the following code.

show(p)




