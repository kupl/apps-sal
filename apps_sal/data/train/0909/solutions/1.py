for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b.sort()
    g.sort()
    ans = []
    flag = 0
    val = 0
    st = 0
    if (b[0] < g[0]):
        f = 'b'
        ans.append(min(b[0], g[0]))
        ans.append(max(b[0], g[0]))
        st = 1
    elif g[0] > b[0]:
        f = 'g'
        st = 1
        ans.append(min(b[0], g[0]))
        ans.append(max(b[0], g[0]))
    else:
        for i in range(n):
            if (b[i] < g[i]):
                f = 'b'
                st = i
                break
            elif g[i] < b[i]:
                st = i
                f = 'g'
                break
            ans.append(b[i])
            ans.append(g[i])
    if (len(ans) == (2 * n)):
        val = 1
    if (n >= 2 and val != 1):
        for i in range(st, n):
            if (f == 'b'):
                ans.append(b[i])
                ans.append(g[i])
            else:
                ans.append(g[i])
                ans.append(b[i])

    for i in range(1, len(ans)):
        if (ans[i] < ans[i - 1]):
            flag = 1
            break
    if (flag):
        print('NO')
    else:
        print("YES")



