import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    s=sum(a)
    if 2*m>s:
        print("T")
    else:
        if s%2==0:
            print("HL")
        else:
            print("T")
