t=int(input())
for i in range(t):
    n=int(input())
    r=0
    while n>0:
        p=n%10
        r=r*10+p
        n//=10
    print(r)

