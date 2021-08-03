def smash(words):
    x = 0
    y = ''
    for elem in words:
        while x < len(words):
            y += words[x] + ' '
            x += 1
    return y[0:-1]
