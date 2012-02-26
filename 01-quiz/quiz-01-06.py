#!/usr/bin/env python

# It looks like I anticipated this question and already solved
# it for the previous section. Perhaps I should be more TDD about it! :)

p = [] # normalized probability distribution
n = 5  # number of cells

for i in range(n):
    p.append(1.0 / n)

print p
