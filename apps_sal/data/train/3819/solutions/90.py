def smash(words):
    s = (' ')
    r = ''
    for i in range(len(words)):
        if i == len(words) - 1:
            r = r + words[i]
        else:
            r = r + words[i] + s
    return r
