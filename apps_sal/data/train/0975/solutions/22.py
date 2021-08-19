for t in range(int(input())):
    (n, r, x, y) = map(int, input().split())
    lx = ly = set()
    if x:
        lx = set(map(int, input().split()))
    if y:
        ly = set(map(int, input().split()))
    F = lx.union(ly)
    if n - len(F) >= r:
        print(r)
    else:
        print(n - len(F))
