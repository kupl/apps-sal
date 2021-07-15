import collections

fact = [1] * 510
MOD = 10 ** 9 + 7
for i in range(2, 502):
 fact[i] = (fact[i - 1] * i) % MOD

for _ in range(int(input())):
 s = input()
 d = collections.Counter(s)
 n = len(s)
 
 num = fact[n]
 den = 1
 for i in d:
  den = (den * fact[d[i]]) % MOD
 
 inv = pow(den, MOD - 2, MOD)
 
 print((num * inv) % MOD)
