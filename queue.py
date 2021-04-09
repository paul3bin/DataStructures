'''
Python code for the implementation of Queue data structure
'''


class Queue:

    # __init__ function definition
    def __init__(self, length):
        self.front = self.current_size = 0
        self.rear = -1
        self.length = length
        self.queue = [None]*length

    def isFull(self):
        return self.length == self.current_size

    def isEmpty(self):
        return self.rear == -1

    def EnQueue(self):
        if self.isFull() is False:
            self.rear += 1
            self.current_size += 1
            self.queue[self.rear] = input(
                'Enter value: ')
        else:
            print('Queue is full!')

    def DeQueue(self):
        if self.isEmpty() is False:
            self.rear -= 1
            self.current_size -= 1
        else:
            print('Queue is empty!')

    def display(self):
        print(self.queue[:self.rear+1])


if __name__ == '__main__':
    print('Queue Data Structure\n')
    response = 'y'
    queueObj = Queue(int(input('Enter the length of the queue: ')))
    print('\n1. Enqueue\n2. Dequeue\n3. Display')
    options = {1: queueObj.EnQueue, 2: queueObj.DeQueue, 3: queueObj.display}
    while(response == 'y'):
        choice = int(input('Option: '))
        if choice not in range(1, 4):
            print('Wrong option. Try again!')
        else:
            options[choice]()
        response = input('Continue? (y/n): ').lower()
