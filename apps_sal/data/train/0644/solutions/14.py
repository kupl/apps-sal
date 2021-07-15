t = int(input())
for i in range(t):
 n = int(input())
 a = [int(k) for k in input().split()]
 if(sum(a) // n == sum(a) / n):
  print('Yes')
 else:
  print('No') 
