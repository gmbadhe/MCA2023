# range() function
'''
To iterate over a sequence of numbers, the built-in function range() is useful
range(10) generates 10 values, the legal indices for items of a sequence of length 10.
It is possible to let the range start at another number, or to specify a
different increment (‘step’)
'''

for i in range(5):
    print(i)
    
print('---------------------------------------------')
print(tuple(range(1, 10)))
print('---------------------------------------------')
print(tuple(range(0, 10, 2)))
print('---------------------------------------------')
print(list(range(-0, -100, -20)))
print('---------------------------------------------')
print(list(range(5)))
print('---------------------------------------------')

s1 = ['I', 'am', 'a', 'student', 'of', 'MIBS']
for i in range(len(s1)):
    print(s1[i], end=" ")
print()
print('---------------------------------------------')
print()
for i in range(len(s1)):
    print(i, s1[i])

