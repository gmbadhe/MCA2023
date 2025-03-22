'''
Global Variables
In Python, a variable declared outside of the function or
in global scope is known as a global variable. This means that
a global variable can be accessed inside or outside of the function.
'''

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local meassage:', message)

greet()

print('Global message :', message)
