def isvalid(s):
    if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        return 1
    return 0


t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    q = int(l[1])
    s = input()
    count = [0 for i in range(n - 2)]
    fre = 0
    for i in range(n - 2):
        if isvalid(s[i:i + 3]):
            fre += 1
        count[i] = fre
    for i in range(q):
        l = input().split()
        L = int(l[0])
        R = int(l[1])
        if R - L + 1 < 3:
            print('NO')
        elif L == 1:
            if count[R - 3] > 0:
                print('YES')
            else:
                print('NO')
        elif count[R - 3] - count[L - 2] > 0:
            print('YES')
        else:
            print('NO')
