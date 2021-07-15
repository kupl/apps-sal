# cook your dish here
for _ in range(int(input())):
    n=int(input())
    k=n
    s=str(n)
    l=len(s)
    su=0
    while k!=0:
        su+=(k%10)**l
        k=k//10
    if su==n:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
