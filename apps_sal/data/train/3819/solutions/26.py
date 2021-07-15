def smash(words):
    res = ""
    for i in range(len(words)):
        res += words[i]
        if i < len(words) - 1: res += ' '
    return res
        

