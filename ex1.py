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

import timeit, matplotlib.pyplot as plt, numpy as np

TASKS = 1000

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

def postorder_with_balance(root):
    if root is None:
        return 0 # if height of subtree is 0
    
    height_left = postorder_with_balance(root.left)
    height_right = postorder_with_balance(root.right)

    balance = height_left - height_right

    print(f"The difference between the left hight and right height (balance measurement) is {balance}")

    return 1 + max(height_left, height_right) # this returns the height. the 1 accounts for the node itself, and max function finds the largest value. If both are 0, then we return 1

def main():
    search_tasks = []
    unshuffled_task = [x for x in range(TASKS)]
    avg_performance, abs_balance = [], []



    for i in range(TASKS):
        task = unshuffled_task[:]
        np.random.shuffle(task)
        search_tasks.append(task)
    for task in search_tasks:
        # find largest absolute balance value
        abs_balance.append(balance)
        total_performance = 0
        for j in range(TASKS):
            total_performance += timeit.timeit(lambda: search(j))
        avg_performance.append(total_performance / TASKS)

    plt.scatter(abs_balance, avg_performance)
    plt.xlabel("Largest Absolute Balance Value")
    plt.ylabel("Average Search Time")
    plt.title("ex1")
    plt.show()

if __name__ == "__main__":
    main()
