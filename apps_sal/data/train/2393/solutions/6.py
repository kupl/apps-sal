def isvalid(l, n):
    for i in range(n):
        for j in range(n):
            if(l[i][j] == '1' and i != n - 1 and j != n - 1 and l[i + 1][j] == '0' and l[i][j + 1] == '0'):
                return 0
    return 1


t = int(input())
for you in range(t):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(s)
    if(isvalid(l, n)):
        print("YES")
    else:
        print("NO")
