n = int(input())

def string_word(word):
    even = ''
    odd = ''
    for j, l in enumerate(word):
        if j % 2 == 0:
            even += l
        else:
            odd+= l
    print("{} {}".format(even, odd))
    
for i in range(n):
    string_word(input())