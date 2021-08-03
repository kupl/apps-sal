import sys

t = eval(input())
for j in range(t):
    n = eval(input())
    a = list(map(int, input().split()))
    ch = 0
    sm = 0
    x = sum(a)
    s1 = [0] * n
    s2 = [0] * n
    for i in range(n):
        sm += a[i]
        s1[i] = sm
        s2[i] = x
        x -= a[i]
    if(sum(a) - a[0] == 0):
        print(0)
    elif(sum(a) - a[n - 1] == 0):
        print(n - 1)
    else:
        for i in range(1, n - 1):
            if(s1[i - 1] == s2[i + 1]):
                print(i)
                ch = 1
                break
        if(ch == 0):
            if(n == 1):
                print(0)
            else:
                print(-1)
