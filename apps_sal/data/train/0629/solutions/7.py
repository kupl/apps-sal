for _ in range(int(input())):
    r1, g1, b1, m = map(int, input().split())
    r = [int(i) for i in input().split()]
    g = [int(j) for j in input().split()]
    b = [int(k) for k in input().split()]
    while m > 0:
        if max(max(r), max(g), max(b)) in r:
            r = [i // 2 for i in r]
        elif max(max(r), max(g), max(b)) in g:
            g = [j // 2 for j in g]
        else:
            b = [k // 2 for k in b]
        m -= 1
    print(max(max(r), max(g), max(b)))
