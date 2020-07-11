# Class for Node
class Node:

    # Initialization function
    def __init__(self,data):
        self.data = data
        self.next = None

# Class for Linked List
class LinkedList:

    #Initialization function
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = None
        else:
            lastNode = self.head
            while(lastNode.next is not None):
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def getCount(self):
        temp = self.head
        count=0
        while(temp):
            count+=1
            temp = temp.next
        return count

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
response = 'y'
LLobject = LinkedList()
while response=='y':
    print('\n----------------------Linked List----------------------')
    print('\n1. Insert\n2. Print linked list')
    choice = int(input('Enter your choice...'))
    if choice==1:
        data = input('Enter data(integer)....')
        LLobject.insert(data)
    elif choice==2:
        print(LLobject.printLinkedList())
    response = input('Want to continue? (y/n)....')