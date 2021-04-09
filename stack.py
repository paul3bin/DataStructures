'''
Python code for stack data-structure
'''


class Stack:

    # Initialization function
    def __init__(self):
        self.stack = []

    # Function to push a value into the stack
    def Push(self):
        self.stack.append(input('Enter value: '))
        print(f'{self.stack[-1]} pushed to stack')

    # Function to pop a value from top of stack
    def Pop(self):
        if self.isEmpty():
            print('Cannot pop from an empty stack!')
        else:
            return self.stack.pop()

    # Function returns true or false based on whether the stack is empty or not.
    def isEmpty(self):
        return not self.stack

    # Function that returns value which is top of stack
    def TopOfStack(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

    # Function that displays value in the stack starting from top to bottom
    def displayStackValues(self):
        print(self.stack[::-1])


if __name__ == '__main__':
    ans = 'y'
    stackObj = Stack()
    print('---------------------------Stack DS---------------------------')
    option = {1: stackObj.Push, 2: stackObj.Pop,
              3: stackObj.displayStackValues}
    while(ans == 'y'):
        print('\n1. Push\n2. Pop\n3. Display')
        res = int(input('Option: '))
        if res not in list(range(1, 4)):
            print('\nWrong option. Try again.')
        else:
            option[res]()
        ans = input('Continue? (y/n): ')
