'''
Python code for the implementation of Queue data structure
'''

class Queue:

    # __init__ function definition
    def __init__(self,length):
        self.front = self.current_size = 0
        self.rear = -1
        self.length = length
        self.queue = [None]*length

    def isFull(self):
        return self.length==self.current_size

    def isEmpty(self):
        return self.rear==-1

    def EnQueue(self):
        if self.isFull() is False:
            self.rear+=1
            self.current_size+=1
            value = input('Enter value to be added to the queue: ')
            self.queue[self.rear]=value
        else:
            print('Queue is full!')

    def DeQueue(self):
        if self.isEmpty() is False:
            self.rear-=1
            self.current_size-=1
        else:
            print('Queue is empty!')

    def display(self):
        print(self.queue[:self.rear+1])

if __name__=='__main__':
    print('Queue Data Structure\n')
    response = 'y'
    length = int(input('Enter the length of the queue: '))
    queueObj = Queue(length)
    print('\n1. Enqueue.\n2. Dequeue.\n3. Display.')
    while(response=='y'):
        choice = int(input('Option: '))
        if choice==1:
            queueObj.EnQueue()
        elif choice==2:
            queueObj.DeQueue()
        elif choice==3:
            queueObj.display()
        else:
            print('Wrong option. Try again.')
        response = input('Continue? (y/n): ').lower()