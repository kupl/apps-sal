"""
import bisect

def insert(list, n): 
    bisect.insort(list, n)  
    return list
"""
t=int(input())
for i in range(0,t):
 n=int(input())

 arr=[]
 brr=[]
 for j in range(0,n):
  x,y=input().split()
  x=int(x)
  y=int(y)
  #insert(arr,x-y)
  #insert(brr,x+y)
  arr.insert(0,x-y)
  brr.insert(0,x+y)
 arr.sort()
 brr.sort()
 m1=arr[1]-arr[0]
 for k in range(1,n-1):
  if((arr[k+1]-arr[k])<m1):
   m1=arr[k+1]-arr[k]
 m2=brr[1]-brr[0]
 for k in range(1,n-1):
  if((brr[k+1]-brr[k])<m2):
   m2=brr[k+1]-brr[k]
 if((min(m1,m2))%2==0):
  print((min(m1,m2))//2)
 else:
  print((min(m1,m2))/2)

