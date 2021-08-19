# cook your dish here
t = int(input())
for j in range(0, t):
    m, n = list(map(int, input().split(" ")))
    u, v = list(map(int, input().split(" ")))
    k = int(input())
    s = input()
    p = 0
    q = 0
    for i in range(0, len(s)):
        if s[i] == 'L':
            p -= 1
        elif s[i] == 'R':
            p += 1
        elif s[i] == 'U':
            q += 1
        elif s[i] == 'D':
            q -= 1
    if p < 0 or p > m or q < 0 or q > n:
        print("Case " + str(j + 1) + ": " + "DANGER")
    elif p == u and q == v:
        print("Case " + str(j + 1) + ": " + "REACHED")
    else:
        print("Case " + str(j + 1) + ": " + "SOMEWHERE")
