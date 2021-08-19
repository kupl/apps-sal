# cook your dish here
try:
    w = 1
    t = int(input())
    for i in range(0, t):
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
            print("Case " + str(w) + ": " + "DANGER")
        elif p == u and q == v:
            print("Case " + str(w) + ": " + "REACHED")
        else:
            print("Case " + str(w) + ": " + "SOMEWHERE")
        w += 1

except:
    pass
