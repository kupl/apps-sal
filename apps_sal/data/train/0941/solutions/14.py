# cook your dish here
t = int(input())

for i in range(t):
 a,b = list(map(int,input().split()))
 
 x=min(a,b)
 y=max(a,b)
 count=0
 #print(x)
 
 for i in range(1,x+1):
  for j in range(1,y+1):
   
   if (i+j) %2 ==0:
    # print(i,j)
    count+=1
    
 print(count)


