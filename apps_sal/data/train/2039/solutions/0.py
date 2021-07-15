import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))


MIN=0
MAX=m

while MIN!=MAX:
    x=(MIN+MAX)//2
    #print(x,MIN,MAX)
    #print()

    M=0
    for a in A:
        #print(a,M)
        if a<=M and a+x>=M:
            continue
        elif a>M and a+x>=m and (a+x)%m>=M:
            continue
        elif a>M:
            M=a
        else:
            MIN=x+1
            break
    else:
        MAX=x

print(MIN)

