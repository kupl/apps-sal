def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    p=x*y
    g=computeGCD(x,y)
    l=p//g
    print((l//x)+(l//y)-2)
        
            

