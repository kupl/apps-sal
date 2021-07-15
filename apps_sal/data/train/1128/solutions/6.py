t=eval(input())

def f(arr):
 
 su = 0
 leftsum = 0
 su=sum(a)
 
 for i in range(n):
  su -= arr[i]
 
  if(leftsum == su):
   return i
 
  leftsum += arr[i]
 
 
 
 return -1

for i in range(t):
 n=eval(input())
 a=list(map(int,input().split()))
 print(f(a)) 

