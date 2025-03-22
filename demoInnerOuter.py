#demo inner and outer function 

def fun1(a): # outer function
    
    def fun2(): # inner function
        print(a)
    return fun2  # returning function without parentheses

my_func = fun1("Hello, python !")
my_func()  # inner function remembers 'a'



'''
Even after fun1() completes execution, the returned fun2()
function retains access to a, demonstrating a closure.
'''
