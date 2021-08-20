letters = input()
n = int(input())
words = list()
for i in range(n):
    word = input()
    words.append(word)
for word in words:
    l = list(word)
    i = 0
    for letter in l:
        if letter in letters:
            continue
        else:
            print('No')
            i = 1
            break
    if i == 0:
        print('Yes')
    i = 0
