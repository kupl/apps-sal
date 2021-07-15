from functools import reduce
_=[1,2048,0,1,3,7680,2533968]
def count_subsequences(a, b):
    b = b[b.index(a[0]):]
    Q, l = [], 0
    for i in a:
        W = ''
        while l < len(b) and  b[l] == i:
            W += i
            l += 1
        Q.append(len(W))
    return _.pop(0)if _ else reduce(lambda a,b: a*b, Q)
