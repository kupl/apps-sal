import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=n-2
    poss=True
    dec=True
    while i>=0 and poss:
        if dec:
            if a[i]<a[i+1]:
                dec=False
        else:
            if a[i]>a[i+1]:
                poss=False
                i+=1
        i-=1
    print(i+1)

