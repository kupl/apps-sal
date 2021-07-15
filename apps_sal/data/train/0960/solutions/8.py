t=int(input())
while(t):
    n=int(input())
    cnt=1
    for i in range(1,n+1):
        s=""
        for j in range(1,n+1):
            s=s+str(bin(cnt))[2:]+" "
            cnt=cnt+1
        print(s)
    t=t-1

