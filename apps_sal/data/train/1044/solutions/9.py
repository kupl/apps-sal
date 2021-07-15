# cook your dish here
t=int(input())
for a in range (t):
    n=int(input())
    sum=0
    while(n>0):
        r=n%10
        sum=sum+r
        n=n//10
    print(sum)
