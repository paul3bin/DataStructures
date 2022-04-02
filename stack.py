'''
Python code for stack data-structure
'''


class Stack:


    def __init__(self):
        """
        Initialization function
        """
        self.stack = []


    def push_value(self):
        """
        Function to push a value into the stack
        """
        self.stack.append(input('Enter value: '))
        print(f'{self.stack[-1]} pushed to stack')


    def pop_value(self):
        """
        Function to pop a value from top of stack
        """
        if self.is_empty():
            print('Cannot pop from an empty stack!')
        else:
            return self.stack.pop()


    def is_empty(self):
        """
        Function returns true or false based on whether the stack is empty or not.
        """
        return not self.stack


    def top_of_stack(self):
        """
        Function that returns value which is top of stack
        """
        if self.is_empty():
            return -1
        else:
            return self.stack[-1]


    def display_stack_values(self):
        """
        Function that displays value in the stack starting from top to bottom
        """
        print(self.stack[::-1])


if __name__ == '__main__':
    ans = 'y'
    stack_obj = Stack()
    print('---------------------------Stack DS---------------------------')
    option = {1: stack_obj.push_value, 2: stack_obj.pop_value,
              3: stack_obj.display_stack_values}
    
    while(ans == 'y'):
        print('\n1. Push\n2. Pop\n3. Display')
        
        res = int(input('Option: '))
        
        if res not in list(range(1, 4)):
            print('\nWrong option. Try again.')
        
        else:
            option[res]()
        
        ans = input('Continue? (y/n): ')
