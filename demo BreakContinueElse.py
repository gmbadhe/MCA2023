
# break , pass and continue Statements, and else Clauses on Loops

##for num in range(1, 10):
##    if num % 2 == 0:
##        print("Found an Even number", num)
##        continue
##    print("number found : ", num)

##for num in range(1, 10):
##    if num % 2 == 0:
##        print("Found an Even number", num)
##        pass
##    print("number found : ", num)

##for num in range(1, 10):
##    if num % 2 == 0:
##        print("Found an Even number", num)
##        pass
##    print("number found : ", num)

for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


