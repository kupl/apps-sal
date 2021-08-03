for _ in range(int(input())):
    a = int(input())
    ans = 100000
    for i in range(40000):
        t = i + (a // (i + 1))
        if(a % (i + 1) == 0):
            t = t - 1
        if(t < ans):
            ans = t
    if(a == 1):
        ans = 0
    print(ans)
