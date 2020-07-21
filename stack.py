'''
Python code for stack data-structure
'''

class Stack:

    # Initialization function
    def __init__(self):
        self.stack = []

    # Function to push a value into the stack
    def Push(self,data):
        self.stack.append(data)
        print(f'{data} pushed to stack')

    # Function to pop a value from top of stack
    def Pop(self):
        if self.isEmpty():
            print('Cannot pop from an empty stack!')
        else:
            return self.stack.pop()

    # Function returns true or false based on whether the stack is empty or not.
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    # Function that returns value which is top of stack
    def TopOfStack(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]    

    # Function that displays value in the stack starting from top to bottom
    def displayStackValues(self):
        print(self.stack[::-1])

ans='y'
stackObj = Stack()
print('---------------------------Stack DS---------------------------')
while(ans=='y'):
    print('\n1. Push\n2. Pop\n3. Display')
    option = int(input('Option: '))
    if option not in list(range(1,4)):
        print('\nWrong option. Try again.')
    elif option==1:
        stackObj.Push(input('Enter value: '))
    elif option==2:
        stackObj.Pop()
    else:
        stackObj.displayStackValues()
    ans = input('Continue? (y/n): ')