def reverse(a):
    b = ''.join(a)[::-1]
    l = []
    for i in a:
        l.append(b[:len(i)])
        b = b[len(i):]
    return l
