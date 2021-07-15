n=int(input())
for i in range(n):
    t=int(input())
    sum=0
    while(t):
        t1=t//100
        sum+=t1
        t=t%100
        if t>0:
            t1=t//50
            sum+=t1
            t=t%50
        if t>0:
            t1=t//10
            sum+=t1
            t=t%10
        if t>0:
            t1=t//5
            sum+=t1
            t=t%5
        if t>0:
            t1=t//2
            sum+=t1
            t=t%2
        if t>0:
            t1=t//1
            sum+=t1
            t=t%1
    print(sum)
