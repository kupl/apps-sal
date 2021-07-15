def factorize(n):
 factors = []
 for i in range(2, int(n**0.5)+1):
  if n % i == 0:
   cntr = 0
   while n % i == 0:
    cntr += 1
    n //= i
   factors.append(i**cntr)
 if n != 1:
  factors.append(n)
 return factors
 
def recur(arr):
 if len(arr)==k:
  return sum(arr)
 res = float('inf')
 for i in range(len(arr)-1):
  for j in range(i+1,len(arr)):
   temp=arr[:]
   temp.remove(arr[i])
   temp.remove(arr[j])
   temp.append(arr[i]*arr[j])
   res = min(res,recur(temp))
 return res

for i in range(int(input())):
 k,x=list(map(int,input().split()))
 arr = factorize(x)
 if len(arr)<k:
  print(sum(arr)+k-len(arr))
 else:
  print(recur(arr))
 
 

