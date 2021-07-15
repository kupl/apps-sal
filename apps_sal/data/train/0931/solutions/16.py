# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 0
    for i in l:
        if i%2==0:
            ans+=i  
    print(ans)
