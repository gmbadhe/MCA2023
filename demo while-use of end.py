'''
The keyword argument end can be used to avoid the newline
after the output,or end the output with a different string:
Output: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
'''

    
a, b = 0, 1

while a < 1000:
    print(a, end=' ')
    a, b = b, a+b


