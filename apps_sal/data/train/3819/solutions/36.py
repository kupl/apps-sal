def smash(words):
    x = ''
    for i in range(len(words)):
        x = x + words[i] + ' '
    x = x[:-1]
    print(x)
    return x
