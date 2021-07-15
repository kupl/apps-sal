t=int(input())
for _ in range(t):
    x=int(input())
    l=len(str(x))
    sum=0
    for i in str(x):
        sum=sum+int(i)**int(l)
    if sum==x:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
