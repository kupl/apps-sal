def find(r):
    a = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    for i in r:
        a[i] = '1'
    a.reverse()
    b = "".join(a)
    return int(b, 2)
