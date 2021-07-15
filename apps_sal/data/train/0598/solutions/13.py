def Turn(a, n):
 m = max(a)
 for i in range(n):
  a[i] = m - a[i]

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if k > 0:
 Turn(a, n)
 k -= 1
 if k & 1 == 1:
  Turn(a, n)
print(' '.join(map(str,a)))

