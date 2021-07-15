t=int(input())
for i in range(1,t+1):
    t=t-1
    fact=1
    n=int(input())
    for i in range(1,n+1,+1):
        fact=fact*i
    print(fact)
