for i in range(int(input())):

    a, b, c, d = map(int, input().split())
    v1 = d - a
    v2 = d - b
    v3 = d - c

    print(v2, v3, v1)
