for _ in range(int(input())):
    n = int(input())
    mini = ["z"] * 100
    s = list(input().strip())
    ans = min(mini, s)
    t = s[:]
    for i in range(n):
        curr = s[i]
        f = 0
        ind = 0
        temp = s[i]
        for j in range(i):
            if s[j] > curr:
                s.pop(i)
                s.insert(j, temp)
                ans = min(ans, s)
                break
        s = t[:]
    for i in range(n):
        curr = s[i]
        f = 0
        ind = n - 1
        temp = s[i]
        for j in range(i + 1, n):
            if s[j] > curr:
                s.pop(i)
                s.insert(j - 1, temp)
                ans = min(ans, s)
                break
        else:
            s.pop(i)
            s.insert(n - 1, temp)
            ans = min(ans, s)
        s = t[:]
    print(*ans, sep='')
