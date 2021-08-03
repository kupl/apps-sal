for _ in range(int(input())):
    n = int(input())
    r = (n + 1) // 2
    dr = []
    for i in range(r):
        t = " " * i + "*"
        dr.append(t)

    for i in range(r):
        print(dr[i])
    for i in range(r - 2, -1, -1):
        print(dr[i])
