'''
Code for sungly linked list using python.

'''

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

    # Function that adds a new node to the linked list.
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

    # funcion for removing a node from the linked list
    def delete(self):
        temp = self.head
        if temp is None:
            print('Cannot delete from an empty list.')
        else:
            value = int(input('Enter the value to be removed: '))
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
            else:
                while temp is not None:
                    if temp.data==value:
                        break
                    prev = temp
                    temp = temp.next

                if temp is None:
                    print('Value not found!')
                    return
                prev.next = temp.next
                temp = None

    # function for displaying the contents of a linked list.
    def printLinkedList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next

# driver code
if __name__ == '__main__':
        
    response = 'y'
    LLobject = LinkedList()

    while response=='y':
        print('\n----------------------Linked List----------------------')
        print('\n1. Insert\n2. Delete value\n3. Print linked list')
        choice = int(input('Enter your choice...'))
        if choice==1:
            data = int(input('Enter data(integer)....'))
            LLobject.insert(data)
        elif choice==2:
            LLobject.delete()
        elif choice==3:
            print(LLobject.printLinkedList())
        else:
            print('Not a valid option. Try again.')
        response = input('Want to continue? (y/n)....')