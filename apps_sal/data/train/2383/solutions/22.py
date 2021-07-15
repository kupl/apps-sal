import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    a,b=list(map(int,input().split()))
    MIN=min(a,b)
    MAX=max(a,b)

    print(max(MIN*2,MAX)**2)
    


