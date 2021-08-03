t = int(input())
while(t > 0):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = 0
    for i in range(0, n, 2):
        if(s >= 0):
            s += l[i]
        else:
            s -= l[i]
        if(i != n - 1):
            if(s < 0):
                s += l[i + 1]
            else:
                s -= l[i + 1]
    if(abs(s) >= k):
        print(1)
    else:
        print(2)
    t -= 1
