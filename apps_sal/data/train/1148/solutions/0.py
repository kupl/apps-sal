def g(x, y):
    d = x[0] >= y[0] and x[1] >= y[1] and (x[2] >= y[2])
    e = x[0] > y[0] or x[1] > y[1] or x[2] > y[2]
    return d and e


t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if g(a, b) and g(b, c):
        print('yes')
    elif g(a, c) and g(c, b):
        print('yes')
    elif g(b, a) and g(a, c):
        print('yes')
    elif g(b, c) and g(c, a):
        print('yes')
    elif g(c, a) and g(a, b):
        print('yes')
    elif g(c, b) and g(b, a):
        print('yes')
    else:
        print('no')
