x, y = input().split()
x = int(x)
y = int(y)

A = []
n = int()
n = x*(x+1)/2
A = [1,x]

ans= []
for i in range(y):
 a = int(input())




 if((a not in A) and (a>=x)):
  n = n+a-A[-1]
  A[-1]=a
  ans.append(n)
  
 else:
  ans.append(n)
  temp = A[0]
  A[0]=A[-1]
  A[-1]=temp
  
  
for t in ans: 
 print(int(t))
 


