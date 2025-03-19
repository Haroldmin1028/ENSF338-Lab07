"""
1. Implement a binary search tree with insertion and search operations as
seen in class [0.2 pts]
    1. It should extend the template provided on D2L with an insert() and a
        search() method

2. Implement code to measure balance for each node in the tree [0.2 pts]

3. Generate a 1000 random search tasks [0.2 pts]
    1. Generate the list of the first 1000 integers
    2. Generate 1000 different tasks by shuffling the list 1000 times

4. For each task, measure average performance (i.e. across searching each
    integer in the tree) and largest absolute balance value [0.2 pts]

5. Generate a scatterplot with absolute balance on the X axis and search
    time on the Y axis [0.2 pts]
"""

import timeit

class Node: # Represents 
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent 
        self.data = data 
        self.left = left
        self.right = right

