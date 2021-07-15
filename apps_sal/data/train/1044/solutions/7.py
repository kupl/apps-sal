n=int(input())
for t in range (n):
    t=int(input())
    sum=0
    while(t>0):
        sum=sum+t%10
        t=t//10
    print(sum)
