# cook your dish here
from math import gcd,sqrt
for _ in range(int(input())):
        s=0
        f=1
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(len(a)):
                s=gcd(s,a[i])
        if(s==1):
                print(-1)
        else:
                for i in range(2,int(sqrt(s))+1):
                        if(s%i==0):
                                print(i)
                                f=0
                                break;
                if(f==1):
                        
                        print(s)        
                        
             
                
                
        
