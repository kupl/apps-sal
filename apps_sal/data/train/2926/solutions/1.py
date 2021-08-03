def reverse(a):
    s = ''.join(a)[::-1]
    l, x = [], 0
    for i in a:
        l.append(s[x:x + len(i)])
        x += len(i)
    return l
