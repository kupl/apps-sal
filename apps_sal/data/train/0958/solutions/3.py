def fxn(n):
    k=2*n-1
    half=k//2
    print(half*" "+"*")
    if n==1:
        return 
    for i in range(2,n):
        j=2*i-1
        p=j-2
        r=j//2
        d=half-r
        print(d*" "+"*"+" "*p+"*")
    print(k*"*")
        





t=int(input())
for i in range(t):
    n=int(input())
    fxn(n)
