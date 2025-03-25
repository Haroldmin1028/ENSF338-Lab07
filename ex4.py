
import sys
sys.setrecursionlimit(20000)
class Node: # Represents a single element of the BST
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data 
        self.left = left
        self.right = right
        self.pivot = None 
        self.balance = 0
        
def insert(data, root=None):
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

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

# Exercise 3: right rotate for Case 3a
def right_rotate(pivot, son):
    if pivot.parent is not None: # meaning if pivot != root
        ancestor = pivot.parent
        ancestor.left = son
    pivot.left = son.right
    son.right = pivot

# Exercise 3: left rotate for Case 3a
def left_rotate(pivot, son):
    if pivot.parent is not None:
        ancestor = pivot.parent
        ancestor.right = son
    pivot.right = son.left
    son.left = pivot

def lr_rotate(pivot):
    son = pivot.left
    grandson = son.right
    old_parent = pivot.parent
    # Perform left rotation on son
    son.right = grandson.left
    if grandson.left is not None:
        grandson.left.parent = son
    grandson.left = son
    son.parent = grandson

    # Perform right rotation on pivot
    pivot.left = grandson.right
    if grandson.right:
        grandson.right.parent = pivot
    grandson.right = pivot
    pivot.parent = grandson

    # Update the parent of pivot (if any)
    grandson.parent = old_parent
    if old_parent is None:
        return grandson  # New root.
    else:
        if old_parent.left == pivot:
            old_parent.left = grandson
        else:
            old_parent.right = grandson
    return grandson

def rl_rotate(pivot):
    son = pivot.right
    grandson = son.left
    old_parent = pivot.parent
    # Perform right rotation on son
    son.left = grandson.right
    if grandson.right is not None:
        grandson.right.parent = son
    grandson.right = son
    son.parent = grandson

    # Perform left rotation on pivot
    pivot.right = grandson.left
    if grandson.left:
        grandson.left.parent = pivot
    grandson.left = pivot
    pivot.parent = grandson

    # Update the parent of pivot (if any)
    grandson.parent = old_parent
    if old_parent is None:
        return grandson
    else:
        if old_parent.right == pivot:
            old_parent.right = grandson
        else:
            old_parent.left = grandson
    return grandson


def postorder_with_balance(root):
    if root is None:
        return 0 # if height of subtree is 0
    
    height_left = postorder_with_balance(root.left)
    height_right = postorder_with_balance(root.right)

    balance = height_right - height_left
    root.balance = balance

    return 1 + max(height_left, height_right) # this returns the height. the 1 accounts for the node itself, and max function finds the largest value. If both are 0, then we return 1

def test(newnode, root):
    current = newnode
    while current.parent is not None:
        current = current.parent
        if current.balance != 0:
            newnode.pivot = current
            break

    if newnode.pivot is None:
        print("Case #1: Pivot not detected.")
    # change to newnode.pivot.balance == 1 or -1 for ex3 and 4
    elif (newnode.pivot.data > newnode.data and newnode.pivot.balance > 0) or (newnode.pivot.data < newnode.data and newnode.pivot.balance < 0):
        print("Case #2: A pivot exists, and a node was added to the shorter subtree.")

    # Exercise 3: Case 3a now supported, 3b not supported
    elif (newnode.pivot.data < newnode.data and newnode.pivot.balance > 0) or (newnode.pivot.data > newnode.data and newnode.pivot.balance < 0):
        # find son
        son = newnode
        while son.parent != newnode.pivot:
            son = son.parent
        # find grandson
        grandson = newnode
        while grandson.parent != son:
            grandson = grandson.parent

        # Case 3a: node added to outside subtree if:
        # 1. added to left subtree of son and pivot is negative, then do right rotation
        if (newnode.data < son.data and newnode.pivot.balance < 0):
            print("Case #3a: Node was added to outside subtree.")
            right_rotate(newnode.pivot, son)
        # 2. added to right subtree of son and pivot is positive, then do left rotation
        elif (newnode.data > son.data and newnode.pivot.balance > 0):
            print("Case #3a: Node was added to outside subtree.")
            left_rotate(newnode.pivot, son)

        # Case 3b: node added to inside subtree if:
        # 1. added to right subtree of son and pivot is negative, then do LR rotation
        elif (newnode.data > son.data and newnode.pivot.balance < 0):
            print("Case #3b: Node was added to inside subtree.")
            newroot = lr_rotate(newnode.pivot)
            if newnode.pivot.parent is None:
                root = newroot
        # 2. added to left subtree of son and pivot is positive, then do RL rotation
        elif (newnode.data < son.data and newnode.pivot.balance > 0):
            print("Case #3b: Node was added to inside subtree.")
            newroot = rl_rotate(newnode.pivot)
            if newnode.pivot.parent is None:
                root = newroot
        else:
            print("Something went wrong in Case #3.")

    else:
        print("Something went wrong.")
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

def test_1():
    print("Test 1: Insertion into empty tree")
    root = None
    root = insert(5, root)
    newnode = search(5, root)
    print("Expected:\nCase #1: Pivot not detected.\nActual:")
    test(newnode, root)
    postorder_with_balance(root)

def test_2():
    print("\nTest 2: Pivot exists, Insertion into shorter subtree")
    root = None
    insert_list = [5, 7, 6, 9, 3]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #2: A pivot exists, and a node was added to the shorter subtree.\nActual:")
            root = test(newnode, root)
        postorder_with_balance(root)
    inorder(root)

def test_3a():
    print("\n\nTest 3a: Pivot exists, Insertion into taller outside subtree")
    root = None
    insert_list = [10, 5, 2, 1]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #3a: Node was added to outside subtree.\nActual:")
            root = test(newnode, root)
        postorder_with_balance(root)
    inorder(root)

# Exercise 4: Create two test cases, both for 3b
def test_3ba():
    print("\n\nTest 3: Pivot exists, Insertion into taller inside subtree")
    root = None
    insert_list = [5, 4, 3, 6, 7, 9, 8]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #3b: Node was added to inside subtree.\nActual:")
            root = test(newnode, root)
        postorder_with_balance(root)
    inorder(root)

# Exercise 4: Create two test cases, both for 3b
def test_3bb():
    print("\n\nTest 3: Pivot exists, Insertion into taller inside subtree")
    root = None
    insert_list = [60, 40, 80, 20, 50, 95, 10, 30, 35]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #3b: Node was added to inside subtree.\nActual:")
            root = test(newnode, root)
        postorder_with_balance(root)
    inorder(root)

def test_4():
    print("\n\nTest 4: No pivot, Insertion into balanced tree")
    root = None
    insert_list = [5, 4, 7, 9]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #1: Pivot not detected.\nActual:")
            root = test(newnode, root)
        postorder_with_balance(root)
    inorder(root)

def main():
    test_1()
    test_2()
    test_3a()
    test_3ba()
    test_3bb()
    test_4()
  
if __name__ == "__main__":
    main()
