# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 a, b = [], []
 for _ in range(n):
  x, h = input().split()
  a.append(int(x))
  b.append(int(h))
 a = [y - x for x, y in zip(a, a[1:])]
 a = sorted(x + y for x, y in zip([0] + a, a + [0]))
 print(sum(x * y for x, y in zip(a, sorted(b))))
