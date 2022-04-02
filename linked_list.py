'''
Code for sungly linked list using python.

'''

# Class for Node


class Node:

    # Initialization function
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for Linked List


class LinkedList:

    # Initialization function
    def __init__(self):
        self.head = None

    # Function that adds a new node to the linked list.
    def insert(self):
        newNode = Node(input('Enter data: '))
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
                    if temp.data == value:
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
        llist = []
        while(temp is not None):
            llist.append(str(temp.data))
            temp = temp.next
        print('->'.join(llist))

    def reverse_linked_list(self):
        curr = self.head  # a
        prev = None
        # a->b->c->d->None
        while True:
            if curr.next is not None:
                nxt = curr.next  # b
                curr.next = prev  # None<-a
                prev = curr  # a
                curr = nxt  # b
            else:
                break
        curr.next = prev
        self.head = curr


# driver code
if __name__ == '__main__':

    response = 'y'
    LLobject = LinkedList()

    print('\n----------------------Linked List----------------------')
    print('\n1. Insert\n2. Delete value\n3. Print linked list\n4. Reverse Linked List')
    options = {1: LLobject.insert, 2: LLobject.delete,
               3: LLobject.printLinkedList, 4: LLobject.reverse_linked_list}
    while response == 'y':
        choice = int(input('Option...'))
        if choice not in range(1, 5):
            print('Not a valid option. Try again.')
        else:
            options[choice]()
        response = input('Want to continue? (y/n)....')
