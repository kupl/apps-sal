depth, q = list(map(int, input().split()))
r = 1000000007
edges = 0
top = 1
bottom = 2**(depth)
for i in range(1, depth + 1):
    edges = edges + (2**i)
for i1 in range(0, q):
    a = list(map(int, input().split()))
    if len(a) == 1:
        print(edges % r)
    else:
        x = a[1]
        if x == 1:
            top = 2 * top
            bottom = 2 * bottom
            edges = (2 * edges) + depth + 1

        elif x == 2:
            top = top * 2
            bottom = 2 * bottom
            edges = (2 * edges) + depth + 1
        elif x == 3:
            depth = (2 * depth) + 1
            edges = (2 * edges) + top
            top = bottom
        else:
            depth = (2 * depth) + 1
            edges = (2 * edges) + bottom
            bottom = top
