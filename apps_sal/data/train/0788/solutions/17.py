t=int(input())
for i in range(t):
    n=int(input())
    a=n%10
    while(n>=10):
        n=n/10
    b=int(n)
    print(a+b)

