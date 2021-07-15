# cook your dish here
t=int(input())
for i in range(0,t):
 x=[]
 n=int(input())
 for j in range(0,n):
  name=str(input())
  time=int(input())
  s=(time,name)
  x.append(s)
 x=sorted(x,key=lambda x:(x[0],x[1])) 
 for j in range(0,len(x)):
  print(x[j][1])
