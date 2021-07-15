t=int(input())
from itertools import permutations as p
for _ in range(t):
    n=int(input())
    for i in range(2*n+1):
        if i<=n:
            for j in range(n-i):
                print(" ",end="")
            for j in range(n,n-i-1,-1):
                print(j,end="")
            print()
        else:
            for j in range(i-n):
                print(" ",end="")
            for j in range(n,i-n-1,-1):
                print(j,end="")
            print()
            
                
    

