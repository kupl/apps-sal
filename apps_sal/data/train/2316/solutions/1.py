import sys

input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    base=0
    for A in a:
        base^=A
    if base==0:
        print("DRAW")
    else:
        m=base.bit_length()-1
        count=0
        for A in a:
            count+=(A>>m &1==1)
        if n%2==1:
            if count%4==1:
                print("WIN")
            else:
                print("LOSE")
        else:
            print("WIN")

