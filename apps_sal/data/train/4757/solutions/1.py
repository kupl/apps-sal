import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n,m,a,b=list(map(int,input().split()))

    if a*n!=m*b:
        print("NO")
        continue
    ANS=[[0]*m for i in range(n)]

    cind=0

    for i in range(n):
        for j in range(a):
            ANS[i][cind]=1
            cind+=1
            cind%=m

    print("YES")

    for a in ANS:
        print("".join(map(str,a)))
                    
                

    
                
    

