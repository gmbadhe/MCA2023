# Demo -For Loops

words = ['camel', 'windowstation', 'defender']
for word in words:
    print(word, len(word))

# Loop over a slice copy of the entire list.
for word in words[:]: 
    if len(word) == 8:
        words.insert(0, word)

for word in words:
    print(word, len(word), end=",")


