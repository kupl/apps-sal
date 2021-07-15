def ham(x):
 w = 0
 while x:
  w += 1
  x &= x-1
 return w


def num_shuff(w_a, w_b, c):
 #known = {}
 if w_a < 0 or w_b < 0:
  return 0
 if c == 0:
  if w_a == 0 and w_b == 0:
   return 1
  else: 
   return 0
 if (w_a, w_b, c) in known:
  return known[(w_a, w_b, c)]
 c0 = c % 2
 c1 = c >> 1
 res = 0 
 if c0 == 0:
  res += num_shuff(w_a, w_b , c1 ) 
  res += num_shuff(w_a - 1, w_b - 1, c1 - 1 ) 
 else:
  res += num_shuff(w_a - 1, w_b, c1 )
  res += num_shuff(w_a, w_b - 1, c1 ) 
 known[(w_a, w_b, c)] = res
 return res


t = int(input())
known = {}
for _ in range(t):
 a, b, c = list(map(int, input().split()))
 print(num_shuff(ham(a), ham(b), c))

