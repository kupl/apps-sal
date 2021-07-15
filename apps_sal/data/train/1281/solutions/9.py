# cook your dish here
t = int(input())
b=[1,2,3,4,5,6,7]
for i in range(t):
 n = int(input())
 a=list(map(int,input().split())) 
 sevenInt=[]
 revList=a[::-1]
 for j in a:
  if j not in sevenInt:
   sevenInt.append(j)
 if(sevenInt==b and a==revList):
  print('yes')
 else:
  print('no')
 

