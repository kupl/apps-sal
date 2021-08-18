t = int(input())
for i in range(t):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    st = input()
    f = 0
    for i in range(n):
        for j in range(m):
            x = i
            y = j
            for k in range(len(st)):
                if st[k] == 'L':
                    y = y - 1
                elif st[k] == 'R':
                    y = y + 1
                elif st[k] == 'U':
                    x = x - 1
                elif st[k] == 'D':
                    x = x + 1
                if x >= 0 and x < n and y >= 0 and y < m:
                    ll = 0
                else:
                    break
            if x >= 0 and x < n and y >= 0 and y < m:
                f = 1
    if f == 1:
        print("safe")
    else:
        print("unsafe")
