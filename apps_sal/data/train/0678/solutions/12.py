# cook your dish here
n=int(input())
for i in range(n):
 l=int(input())
 m=list(map(int,input().split()))
 j=0
 count=0
 days=0
 p=m[0]+1
 while(j<l):
  days+=1
  try:
   count=count+sum(m[j:j+p])
  except:
   break
  j=j+p
  p=count
 print(days)



   
  
  

