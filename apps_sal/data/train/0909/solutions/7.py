import sys     
import math as mt
import bisect
input=sys.stdin.readline
t=int(input())
#t=1  
   
def solve(l3,l4):
    cnt=0
    l5=[]
    for i in range(n):
        l5.append(l3[i])
        l5.append(l4[i])
    
    for i in range(1,len(l5)):
        if l5[i]<l5[i-1]:
            cnt=1
    if cnt==0:
        return True
    
    return False    
            
   
for _ in range(t):
    n=int(input())
    #n,k=map(int,input().split())
    #x,y,k=map(int,input().split())
    #n,h=(map(int,input().split()))
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    if (solve(l1,l2) or solve(l2,l1)):
        print("YES")
    else:
        print("NO")
                        

