def reverseWords(str):
    k = str.split(' ')
    k.reverse()
    str = ' '.join(k)
    return str
