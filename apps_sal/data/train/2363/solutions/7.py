import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n=int(input())
    S=sorted(map(int,input().split()))

    ANS=1<<30

    for i in range(1,n):
        ANS=min(ANS,S[i]-S[i-1])
    print(ANS)

    

