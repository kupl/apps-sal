# cook your dish here
for _ in range(int(input())):
 n,q=map(int,input().split())
 a=list(map(int,input().split()))
 even,odd=0,0
 for i in range(n):
  c=bin(a[i]).count('1')
  if c%2==0:
   even+=1 
  else:
   odd+=1 
 for j in range(q):
  m=int(input())
  t=bin(m).count('1')
  temp1,temp2=even,odd
  if t%2==0:
   temp1,temp2=even,odd
  else:
   temp1,temp2=odd,even
  print(str(temp1)+" "+str(temp2))
