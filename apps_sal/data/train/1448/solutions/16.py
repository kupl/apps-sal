# cook your dish here
#Author : Ashutosh Wagh, Codechef : ashutosh0903
for _ in range(int(input())) :
    a,d,k,n,inc = list(map(int,input().split()))
    ans = a 
    for i in range(2,n+1) :
        if i%k!=1 :
            ans = ans + d
        else :
            d = d + inc
            ans = ans + d
    print(ans)

