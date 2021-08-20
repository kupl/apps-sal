def smash(words):
    i = 0
    l = len(words)
    str1 = ''
    while i < l:
        if i < l - 1:
            str1 += words[i] + ' '
        else:
            str1 += words[i]
        i += 1
    return str1
