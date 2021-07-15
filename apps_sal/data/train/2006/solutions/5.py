def gcd(a, b):
  return gcd(b, a % b) if b else a

n = int(input())
A = [int(x) for x in input().split()]
A.sort()
g = 0
for x in A:
  g = gcd(x, g);
print("Alice" if (A[n-1]//g-n) % 2 else "Bob")

