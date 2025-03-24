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

    return root

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

def postorder_with_balance(root, balances):
    if root is None:
        return 0 # if height of subtree is 0
    height_left = postorder_with_balance(root.left, balances)
    height_right = postorder_with_balance(root.right, balances)
    balance = height_right - height_left # fixed, was reverse before (L-R)
    balances.append(abs(balance))
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
        root = None
        for value in task:
            root = insert(value, root)
        balances = []
        postorder_with_balance(root, balances)
        abs_balance.append(max(balances))
        total_performance = 0
        for j in range(TASKS):
            total_performance += timeit.timeit(lambda: search(j, root), number = 1)
        avg_performance.append(total_performance / TASKS)

    plt.scatter(abs_balance, avg_performance)
    plt.xlabel("Largest Absolute Balance Value")
    plt.ylabel("Average Search Time")
    plt.title("ex1")
    plt.show()

if __name__ == "__main__":
    main()
