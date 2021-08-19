def maxi(a, b):
    if bin(a).count('1') == bin(b).count('1'):
        return min(a, b)
    elif bin(a).count('1') > bin(b).count('1'):
        return a
    else:
        return b


t = int(input().rstrip())
for i in range(t):
    (a, b) = list(map(int, input().rstrip().split(' ')))
    x = bin(a)[2:]
    y = bin(b)[2:]
    w = max(len(x), len(y))
    x = '0' * (w - len(x)) + x
    y = '0' * (w - len(y)) + y
    q = [0 for i in range(w)]
    for j in range(w):
        if x[j] != y[j]:
            q[j] = '0'
            break
        else:
            q[j] = x[j]
    for o in range(j + 1, w):
        q[o] = '1'
    e = int('0b' + ''.join(q), 2)
    print(maxi(e, b))
