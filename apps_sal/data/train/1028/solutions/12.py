def arm(n):
    sum=0
    l=len(str(n))
    m=n
    while n!=0:
        sum+=(n%10)**l
        n//=10
    if sum==m:
        return "FEELS GOOD"
    else:
        return "FEELS BAD"

t=int(input())
l=[]
for i in range(t):
    l.append(arm(int(input())))
for i in l:
    print(i)


