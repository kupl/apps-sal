def smash(words):
    a = ""
    for c,i in enumerate(words):
        if c == len(words)-1:
            a += i
        else:
            a += i + " "
    return a

