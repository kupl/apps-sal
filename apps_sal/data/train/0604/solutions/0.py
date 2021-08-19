for _ in range(int(input())):
    (r, c) = map(int, input().split())
    l = []
    for k in range(r):
        a = list(map(int, input().split()))
        l.append(a)
    ans = 'Stable'
    for i in range(r):
        for j in range(c):
            p = l[i][j]
            count = 0
            if i - 1 >= 0 and j >= 0:
                count += 1
            if i >= 0 and j - 1 >= 0:
                count += 1
            if i + 1 <= r - 1 and j <= c - 1:
                count += 1
            if i <= r - 1 and j + 1 <= c - 1:
                count += 1
            if count <= p:
                ans = 'Unstable'
                break
    print(ans)
