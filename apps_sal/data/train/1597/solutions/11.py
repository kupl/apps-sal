# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:50:29 2020

@author: Vineet
"""


from math import sqrt

t=int(input())

while(t>0):
 a,m = [int(x) for x in input().split()]
 div=[]
 n=[]
 for i in range(1,int(sqrt(m))+1):
  if m%i==0:
   if m//i==i:
    div.append(i)
   else:
    div.append(i)
    div.append(m//i)
 div.sort()
 div=div[:-1]
 
 for i in div:
  if ((m//i)-1)%a==0:
   n.append(i*(((m//i)-1)//a))
 s=set(n)
 n=list(s)
 n.sort()
 print(len(n))
 for i in n:
  print(i,end=' ')
 print()

 t-=1
