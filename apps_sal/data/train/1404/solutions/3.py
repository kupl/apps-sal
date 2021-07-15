t = eval(input())
for _ in range(t):
 r, g, b = list(map(int, input().split()))
 k = eval(input())
 d = {}
 d['R'] = r
 d['G'] = g
 d['B'] = b
 c = 0
 r = {'r':0, 'g':0, 'b':0}
 while r['r'] != k or r['g'] != k or r['b'] != k:
  if d['R'] > 0 and k > 0:
   d['R'] -= 1
   r['r'] += 1
   c += 1
   if r['r'] == k or r['g'] == k or r['b'] == k:
    break
  if d['G'] > 0 and k > 0:
   d['G'] -= 1
   r['g'] += 1
   c += 1
   if r['r'] == k or r['g'] == k or r['b'] == k:
    break
  if d['B'] > 0 and k > 0:
   d['B'] -= 1
   r['b'] += 1
   c += 1
   if r['r'] == k or r['g'] == k or r['b'] == k:
    break
 print(c)
