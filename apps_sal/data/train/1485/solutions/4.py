for t in range(int(input())):
    n = int(input())
    p1 = 0
    p2 = 0
    ans = 500
    diff = []
    for i in range(n):
        a = input()
        x = 0
        y = 0
        for j in range(n // 2):
            if a[j] == '1':
                p1 += 1
                x += 1
        for j in range(n // 2, n):
            if a[j] == '1':
                p2 += 1
                y += 1
        diff.append(2 * (y - x))
    for k in range(n):
        ans = min(ans, abs(p1 - p2 + diff[k]))
    print(min(ans, abs(p1 - p2)))
