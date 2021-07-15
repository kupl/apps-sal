t=int(input())
for i in range(t):
    n=int(input())
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    print(fact)
