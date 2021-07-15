#cook your dish here
for _ in range(int(input())):
    n = int(input())
    ans = 0
    ar = list(map(int,input().split()))
    for i in range(n):
        if ar[i]%2==0:
            ans+=ar[i]
    print(ans)
