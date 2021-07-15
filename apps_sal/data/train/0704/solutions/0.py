# cook your dish here
for _ in range(int(input())):
    a,n,m = map(int,input().split(' '))
    s = len(str(a))
    #print(s)
    c = 10**s - 1
    w = c*m
    b = pow(10,n*s,w)-1
    d = b//c
    ans = (d%m)*(a%m)
    print(ans%m)  
