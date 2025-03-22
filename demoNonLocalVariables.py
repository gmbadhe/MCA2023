#Nonlocal Variables
'''
In Python, the nonlocal keyword is used within nested functions
to indicate that a variable is not local to the inner function,
but rather belongs to an enclosing function’s scope.
This allows you to modify a variable from the outer function
within the nested function, while still keeping it distinct
from global variables.
'''

# outside function 
def outer():
    message = 'localVariable-Content'

    # nested function  
    print("outer1:", message)
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'non-localVriables-Content'
        print("inner:", message)

    inner()
    print("outer:", message)
    #inner()
outer()





'''
Here is a nested inner() function.
The inner() function is defined in the scope of another function outer().
We have used the nonlocal keyword to modify the message variable
from the outer function within the nested function.
'''

