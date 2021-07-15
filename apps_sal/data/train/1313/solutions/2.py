# cook your dish here
import math

for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    if l[0]==1:
        print(-1)
        
    else:
        l1=[l[0]]
        flag=0
        for i in range(1, n):
            p=math.gcd(l1[-1], l[i])
            if p==1:
                print(-1)
                flag=1 
                break
            
            else:
                l1.append(p)

        if flag==0:
            p=l1[-1]
            for i in range(2, int(p**0.5)+1):
                if p%i==0:
                    print(i)
                    flag=1 
                    break
                
        if flag==0:
            print(p)
