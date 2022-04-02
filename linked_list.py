'''
Code for sungly linked list using python.

'''


class Node:
    """
    Class for a linked list node.
    """
    def __init__(self, data):
        """
        Initialization function
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Class for a linked list
    """

    def __init__(self):
        """
        Initialization function
        """
        self.head = None

    def insert(self):
        """
        function that adds a new node to the linked list.
        """
        newNode = Node(input('Enter data: '))
        if self.head is None:
            self.head = newNode
            self.head.next = None
        else:
            lastNode = self.head
            while(lastNode.next is not None):
                lastNode = lastNode.next
            lastNode.next = newNode

    def delete(self):
        """
        funcion for removing a node from the linked list
        """
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

    def print_linked_list(self):
        """
        function for displaying the contents of a linked list.
        """
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
