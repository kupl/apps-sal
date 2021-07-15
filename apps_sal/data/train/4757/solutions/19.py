import math
t=int(input())
def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
      
for i in range(t):
    n,m,a,b=map(int,input().split())
    if m*b!=n*a:
        print('NO')
    else:
        print('YES')
        l=0
        for j in range(n):
            ans=['0']*m
            for k in range(a):
                ans[(l+k)%m]='1'
            print(convert(ans))
            l+=math.gcd(a,m)
