'''
Python code for Binary Search Tree
'''

class Node:
    left=right=None
    # initialization function
    def __init__(self,value):
        self.value = value

# A function to insert a new node with given value.
def insert(root,value):
    if root is None:
        root = Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left,value)
        else:
            root.right = insert(root.right,value)
    return root

# A function to search the given value in a Binary Search Tree.
def search(root,value):
    # First condition: if Root is None or value is present at root then return root.
    if root is None or root.value==value:
        return 'Search value found! {}'.format(value)
    # If given value is greater than root value.
    elif root.value < value:
        return search(root.right,value)
    # If given value is less than root value.
    else:
        return search(root.left,value)

def inorder(root):
    # inorder traversal: left,root,right
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    # postorder traversal: left,right,root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def preorder(root):
    # preorder traversal: root,left,right
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

print('\n-----------------Binary Search Tree-----------------')
val = int(input('Enter root value: '))
root = Node(val)
response = 'y'
while response=='y':
    print('\n1. Insert\n2. Search\n3. Print In-Order\n4. Print Post-Order\n5. Print Pre-Order')
    option = int(input('\nOption...'))
    if option not in list(range(1,6)):
        print('\nWrong option. Try again.')
    else:
        if option==1:
            value = int(input('Enter value: '))
            insert(root,value)
        elif option==2:
            print(search(root,int(input('Enter value to be searched: '))))
        elif option==3:
            inorder(root)
        elif option==4:
            postorder(root)
        else:
            preorder(root)
    response = input('continue?(y/n): ')