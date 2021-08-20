t = int(input())
for z in range(t):
    (n, r, x, y) = map(int, input().split())
    if x != 0 and y != 0:
        lx = set(map(int, input().split()))
        ly = set(map(int, input().split()))
    elif x == 0 and y != 0:
        ly = set(map(int, input().split()))
    elif x != 0 and y == 0:
        lx = set(map(int, input().split()))
    if x == 0 and y == 0:
        if n <= r:
            print(n)
        else:
            print(r)
    elif x == 0 and y != 0:
        if n - y <= r:
            print(n - y)
        else:
            print(r)
    elif x != 0 and y == 0:
        if n - x <= r:
            print(n - x)
        else:
            print(r)
    else:
        p = len(lx.union(ly))
        if n - p <= r:
            print(n - p)
        else:
            print(r)
