def subset_sum_check(l, n, sum1):
 while n >= 0:
  if sum1 - l[n] == 0:
   return True
  elif sum1 - l[n] > 0:
   if subset_sum_check(l, n - 1, sum1 - l[n]):
    return True
  n -= 1
 return False
 
for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 arr = [int(i) for i in input().split()]
 h=n//2
 if n%2!=0:
  h+=1 
 if k>=h:
  k=n-k
 arr.sort()
 print(abs(sum(arr[:k])-sum(arr[k:])))

