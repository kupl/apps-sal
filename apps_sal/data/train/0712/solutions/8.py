import math
def gcd(a,b): 
 if (b == 0): 
   return a 
 return gcd(b, a%b) 

def lcm(a,b): 
 return (a*b) / gcd(a,b) 

def bs(arr, l, r, x): 
 while l <= r: 
  mid = l + (r - l)//2; 
  if(arr[mid]==x): 
   return arr[mid]
  elif(arr[mid]<x): 
   l = mid + 1
  else: 
   r = mid - 1
 return -1

def swap(list, pos1, pos2): 
  
 list[pos1], list[pos2] = list[pos2], list[pos1] 
 return list

t = int(input())
for _ in range(t):
 n = int(input())
 a = list(map(int,input().split()))
 f = 0
 for i in range(n):
  if(a[i]%2==0):
   f=1
 if(f):
  print('NO')
 else:
  print('YES')
