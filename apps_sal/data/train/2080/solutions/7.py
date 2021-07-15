m = int(input())
q = [int(i) for i in input().split()]

n = int(input())
a = [int(i) for i in input().split()]
c = min(q)
a.sort()

price = 0
for i in range(n):
  if i % (c+2) < c:
    price += a[n-1-i]
  
print(price)
