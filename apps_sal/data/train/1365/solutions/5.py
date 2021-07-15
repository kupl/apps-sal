from functools import lru_cache


def rle(s):
 if not s:
  return []
 last = s[0]
 count = 0
 for curr in s:
  if last == curr:
   count += 1
  else:
   yield (last, count)
   count = 1
   last = curr
 else:
  yield (last, count)


@lru_cache(maxsize=None)
def fact(n):
 if n < 3:
  return max(1, n)
 return n * fact(n - 1)


def comb_count(n):
 ans = 0
 for repl_length in range(0, n + 1, 2):
  n_fs = n - repl_length
  n_cs = repl_length >> 1
  ans += fact(n_fs + n_cs) // (fact(n_fs) * fact(n_cs))
 return ans


s = input()
ans = 1
if 'c' not in s and 'k' not in s:
 for (char, count) in rle(s):
  if char in 'gf':
   ans *= comb_count(count)
 print(ans)
else:
 print(0)
