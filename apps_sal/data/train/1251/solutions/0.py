import sys

def _r(*conv) :
 r = [conv[i](x) for i, x in enumerate(input().strip().split(' '))]
 return r[0] if len(r) == 1 else r

def _ra(conv) :
 return list(map(conv, input().strip().split(' ')))

def _rl() :
 return list(input().strip())

def _rs() :
 return input().strip()

def _a(k, *v) :
 return all(x == k for x in v)

def _i(conv) :
 for line in sys.stdin :
  yield conv(line)
##################################################################

n = _r(int)
lookup = dict([(x, i) for i, x in enumerate(_ra(str))])
g = [(set(), dict()) for _ in range(n)]

m = _r(int)
for _ in range(m) :
 c1, c2, d = _r(str, str, int)
 i1 = lookup[c1]

 g[i1][0].add(c2)
 g[i1][1][c2] = d


t = _r(int)
for _ in range(t) :
 k = _ra(str)[1:]
 
 failed = False
 if len(set(k)) != len(k) :
  failed = True

 if not failed :
  if k[0] not in lookup : 
   failed = True
  else : 
   r = 0
   v = g[lookup[k[0]]]

   for i in range(1, len(k)) : 
    if k[i] not in v[0] : 
     failed = True
     break

    r += v[1][k[i]]
    v = g[lookup[k[i]]]
   
   if not failed : 
    print(r)
  
 if failed : 
  print('ERROR')

