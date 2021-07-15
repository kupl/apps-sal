N, M = map(int, input().split())
A = list(map(int, input().split()))
a = sum(A)
base = 10 ** 9 + 7
# * pow(a, base-2, base) # equivalent to division by a

# ans = comb(M+N, a+N)

def fact(x):
  r = 1
  for i in range(1,x+1):
    r *= i
    r %= base
  return r

ans = 1
for i in range(a+N):
  ans *= M+N-i
  ans %= base
ans *= pow(fact(a+N), base-2, base)
ans %= base
print(ans)
