#!/usr/bin/env python

#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

# According to lecture this is called the "measurement update" function.
def sense(p, Z):
    q = []
    for i in range(len(p)):
        if world[i] == Z:
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    total = sum(q)
    return map((lambda(x): x/total), q)

print sense(p,Z)
