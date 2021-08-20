t = int(input())
for i in range(t):
    (n, r, x, y) = list(map(int, input().strip().split(' ')))
    X = []
    Y = []
    if x != 0:
        X = list(map(int, input().strip().split(' ')))
    if y != 0:
        Y = list(map(int, input().strip().split(' ')))
    X.extend(Y)
    X = set(X)
    l = n - len(X)
    if r < l:
        print(r)
    else:
        print(l)
