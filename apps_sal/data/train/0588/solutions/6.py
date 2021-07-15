def find_gcd(x, y):
 while y:
  x, y = y, x % y

 return x


T = int(input())

for i in range(T):
 N = int(input())
 lst = [int(x) for x in input().strip().split()]
 diff = []

 for j in range(1, len(lst)):
  diff.append(lst[j] - lst[j - 1])

 diff.append(360)

 gcd = find_gcd(diff[0], diff[1])
 for j in range(2, len(diff)):
  gcd = find_gcd(gcd, diff[j])

 print(360 // gcd - N)

