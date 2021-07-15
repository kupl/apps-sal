
from collections import defaultdict
import os
import sys
from io import BytesIO, IOBase


def binarySearchCount(arr, n, key): 
 
 left = 0
 right = n - 1
 
 count = 0
 
 while (left <= right):  
  mid = int((right + left) / 2) 
 
  # Check if middle element is 
  # less than or equal to key 
  if (arr[mid] <= key):  
 
   # At least (mid + 1) elements are there 
   # whose values are less than 
   # or equal to key 
   count = mid + 1
   left = mid + 1
   
  # If key is smaller, ignore right half 
  else: 
   right = mid - 1
  
 return count 
def can_break(N,a,d,x,y,maxi,mini):
 c=x+y
 if c<mini:
  return 0
 if c in d:
  return -1
 
 if c>maxi:
  return N 
 
 x=binarySearchCount(a,N,c)
 return x
 """
    mid=(N-1)//2
    if c<a[mid]:
     count=0
     for i in a:
      if i>c:
       return count
      count+=1
  
    else:
     count=mid+1
     for i in range(mid+1,N):
      if a[i]>c:
       return count
      count+=1
    """ 

T=int(input())
while T:
 N=int(input())
 a=tuple(map(int,input().split()))
 d=defaultdict()
 mini=a[0]
 maxi=a[-1]
 for i in range(N):
  d[a[i]]=i
 Q=int(input())
 while Q:
  x,y=list(map(int,input().split()))
  if x==0 and y==0:
   print(0)
  else:
   print(can_break(N,a,d,x,y,maxi,mini))
  Q-=1
 T-=1 

