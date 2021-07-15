alph="abcdefghijklmnopqrstuvwqyz"
def solve(s,i,n):
    if n==1:
        if s[0]==alph[i]:
            return 0
        else:
            return 1
    else:
        c1=0
        c2=0
        s1=s[0:n//2]
        s2=s[n//2:n]
        for x in s1:
            if x!=alph[i]:
                c1+=1
        for x in s2:
            if x!=alph[i]:
                c2+=1
        return min(c1+solve(s2,i+1,n//2),c2+solve(s1,i+1,n//2))
import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    s=input()
    s=s[0:n]
    print(solve(s,0,n))
