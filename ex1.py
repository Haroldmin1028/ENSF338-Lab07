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

class Node: # Represents a single element of the BST
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent 
        self.data = data 
        self.left = left
        self.right = right


def insert(data, root=None): # (part 1)
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data: 
            current = current.left
        else:
            current = current.right # current becomes none eventually (leaf position is found) (insertion point)

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode

def search(data, root): # (part 1)
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

def height(root):
    if root is None
