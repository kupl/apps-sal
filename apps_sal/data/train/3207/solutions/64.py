def reverseWords(s):
    a = s.split()
    a.reverse()
    b = a[0]
    a.pop(0)
    for x in a:
        b = b + ' ' + x
    return b
