for t in range(int(input())):
    total = 0

    def check(n, store):
        nonlocal edges, q, points
        if n in store:
            return
        for i in range(q):
            if n == edges[i][0]:
                edges[i][0] = -1
                x = edges[i][1]
                edges[i][1] = -1
                if x in points:
                    check(x, store + [n])
            elif n == edges[i][1]:
                edges[i][1] = -1
                x = edges[i][0]
                edges[i][0] = -1
                if x in points:
                    check(x, store + [n])
        points.remove(n)
    n, q = list(map(int, input().split()))
    edges = []
    points = [i for i in range(n)]
    for i in range(q):
        x = input().split()
        edges.append([int(x[0]), int(x[1])])
    for i in range(n):
        if i in points:
            total += 1
            check(i, [])
    print(total)
