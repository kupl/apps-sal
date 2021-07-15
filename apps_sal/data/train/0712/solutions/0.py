def gcd(a,b):
 if b==0: return a
 return gcd(b,a%b)

for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 value = arr[0]
 if n!=1:
  for i in arr[1:]:
   value = value*i//gcd(value, i)
 if value%2==0:
  print("NO")
 else:
  print("YES")
