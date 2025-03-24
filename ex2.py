class Node: # Represents a single element of the BST
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data 
        self.left = left
        self.right = right
        self.pivot = None # added
        self.balance = 0 # added
        
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

def postorder_with_balance(root):
    if root is None:
        return 0 # if height of subtree is 0
    
    height_left = postorder_with_balance(root.left)
    height_right = postorder_with_balance(root.right)

    balance = height_right - height_left
    root.balance = balance

    return 1 + max(height_left, height_right) # this returns the height. the 1 accounts for the node itself, and max function finds the largest value. If both are 0, then we return 1

def test(newnode):
    # exercise 2 - identify pivot node on node insertion
    current = newnode
    while current.parent is not None:
        current = current.parent
        if current.balance != 0:
            newnode.pivot = current
            break

    # exercise 2 - identify case 1
    if newnode.pivot is None:
        print("Case #1: Pivot not detected.")
    # exercise 2 - identify case 2
    elif (newnode.pivot.data > newnode.data and newnode.pivot.balance > 0) or (newnode.pivot.data < newnode.data and newnode.pivot.balance < 0):
        print("Case #2: A pivot exists, and a node was added to the shorter subtree.")
    # exercise 2 - identify case 3
    elif (newnode.pivot.data < newnode.data and newnode.pivot.balance > 0) or (newnode.pivot.data > newnode.data and newnode.pivot.balance < 0):
        print("Case #3: Not supported.")
    else:
        print("Something went wrong.")


def test_1():
    print("Test 1: Insertion into empty tree")
    root = None
    root = insert(5, root)
    newnode = search(5, root)
    print("Expected:\nCase #1: Pivot not detected.\nActual:")
    test(newnode)
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
            test(newnode)
        postorder_with_balance(root)

def test_3():
    print("\nTest 3: Pivot exists, Insertion into taller subtree")
    root = None
    insert_list = [5, 4, 3, 6, 7, 8, 9]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #3: Not supported.\nActual:")
            test(newnode)
        postorder_with_balance(root)

def test_4():
    print("\nTest 4: No pivot, Insertion into balanced tree")
    root = None
    insert_list = [5, 4, 7, 9]
    for value in insert_list:
        root = insert(value, root)
        if value == insert_list[-1]:
            newnode = search(insert_list[-1], root)
            print("Expected:\nCase #1: Pivot not detected.\nActual:")
            test(newnode)
        postorder_with_balance(root)

def main():
    test_1()
    test_2()
    test_3()
    test_4()
  
if __name__ == "__main__":
    main()
