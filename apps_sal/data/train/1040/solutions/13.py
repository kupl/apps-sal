t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    s = input()
    if n < 3:
        for i in range(m):
            a, b = list(map(int, input().split()))
            print('NO')
    else:
        k = [s[0], s[1], s[2]]
        if k[0] == k[1] or k[1] == k[2] or k[0] == k[2]:
            c = 1
        else:
            c = 0
        ans = [0, c]
        for i in range(3, n):
            del(k[0])
            k.append(s[i])
            if k[0] == k[1] or k[1] == k[2] or k[0] == k[2]:
                c += 1
            ans.append(c)
        for i in range(m):
            a, b = list(map(int, input().split()))
            if b - a < 2:
                print('NO')
                continue
            b -= 2
            a -= 1
            if ans[b] - ans[a] == 0:
                print('NO')
            else:
                print('YES')
