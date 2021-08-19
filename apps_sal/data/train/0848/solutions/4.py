"""t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))
    if(n==3):
        print(l[0]+l[1]+l[2])
    elif(n==4):
        print(sum(l)-min(l))
    else:
        ans=0
        for i in range(n):
            k = [0 for i in range(5)]
            k[0]=l[i]
            k[1]=l[(i+n+1)%n]
            k[2] = l[(i+n+2)%n]
            k[3] = l[i-1]
            k[4] = l[i-2]
            k.sort()
            p = k[2]+k[3]+k[4]
            if(p>ans):
                ans=p
        print(ans)"""
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))
    if n == 3:
        print(sum(l))
    else:
        ans = 0
        for j in range(n):
            p = l[j] + l[(j + n + 1) % n] + l[(j + n + 2) % n]
            if p > ans:
                ans = p
        p = l[n - 2] + l[n - 1] + l[0]
        if p > ans:
            ans = p
        p = l[1] + l[n - 1] + l[0]
        if p > ans:
            ans = p
        print(ans)
