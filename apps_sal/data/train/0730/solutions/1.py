# cook your code here
for _ in range(eval(input())):
 n=eval(input())
 ind=0
 m=0
 
 for i in range(n):
  
  l=[int(x) for x in input().split()]
  sc=l[0]
  for j in range(1,len(l)):
   sc+=int(l[j]>=4)+int(l[j]>=5)+2*int(l[j]>=6)
  if sc==m:
   ind=-2
  if sc>m :
   m=sc
   ind=i+1
  
   
 if (ind==-2):
  print("tie")
 elif (ind==1) :
  print("chef")
 else:
  print(ind)
