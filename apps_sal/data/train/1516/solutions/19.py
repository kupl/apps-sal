MOD = 1000000007
for _ in range(int(input())):
 n, k = map(int, input().split())
 last_term = k - 1
 if n == 2:
  ans = (last_term * (last_term + 1)) // 2
  print(ans % MOD)

 else:
  diff = n - 1
  first_term = last_term%diff
  if first_term==0:
   first_term = diff
  no_of_terms = (last_term - first_term) // diff + 1
  ans = ((2*first_term+((no_of_terms - 1) * diff)) * no_of_terms) // 2
  print(ans % MOD)
