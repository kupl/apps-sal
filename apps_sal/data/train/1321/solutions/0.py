T=int(input())
for i in range(T):
    n=int(input())
    if n==1:
        print("0")
    else:
        n=n-2
        l=(n+1)*(2*n+3)*(n+2)/6
        print(int(l))

