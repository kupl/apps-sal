for t in range(int(input())):
 s = input().split()
 d, loc, p = {}, [], 0
 for x in range(6):
  if s[x] in d: d[s[x]].append(x)
  else: d[s[x]] = [x]
 for i in d:
  if len(d[i]) >= 3:
   loc = d[i]
   break
 for l in range(0, 5, 2):
  if l in loc or (l + 1) in loc: p += 1
 if p == 3: print('YES')
 else: print('NO')
