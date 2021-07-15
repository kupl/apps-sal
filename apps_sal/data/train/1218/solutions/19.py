n=int(input())
for i in range(n):
    sum1=0
    a,b=map(int,input().split())
    for x in range(a,b,a):
        sum1+=x
    print(sum1)
