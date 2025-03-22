''' 
Local Variables
When we declare variables inside a function, these variables will have
a local scope (within the function).
We cannot access them outside the function.
'''

message='welcome'
def greet():
    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

print(message)
