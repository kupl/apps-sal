for i in range(int(input())):
    n = int(input())
    rows = []
    for i in range(n):
        rows.append(list(map(int, input().split())))
    c = max(rows[-1])
    add = c
    try:
        for j in range(n - 2, -1, -1):
            c = max([i for i in rows[j] if i < c])
            add += c
        print(add)
    except ValueError:
        print(-1)
