import sys

def __starting_point():
 t = int(input())
 for i in range(t):
  n=int(input())
  s1=input()
  s=0
  a1=[]
  a2=[]
  for i in range(n):
   a1.append(s)
   s=s^1
  s=1
  for i in range(n):
   a2.append(s)
   s = s ^ 1
  c1=0
  c2=0
  for i in range(n):
   if(int(s1[i])!=a1[i]):
    c1+=1
  for i in range(n):
   if(int(s1[i])!=a2[i]):
    c2+=1
  print(min(c1,c2))






__starting_point()
