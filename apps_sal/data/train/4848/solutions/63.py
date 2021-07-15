def char_freq(message):
    a = {}
    for i in message:
        if i not in a:
            a.setdefault(i,1)
        else:
            a[i]+=1
    return a
