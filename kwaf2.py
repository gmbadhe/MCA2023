#To write a function that accepts any number of positional arguments
# using a * argument.

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(34,56))

print(avg(3,23,34,45,56,67,78,1))
