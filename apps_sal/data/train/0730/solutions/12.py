t = int(input())
for _ in range(t):
 n = int(input())
 c = []
 for _ in range(0,n):
  c.append(list(map(int,input().split())))
 s = []
 for i in c:
  s.append(len(set(i[1:])))
 for i in range(len(s)):
  if s[i] == 4:
   s[i] = 1+c[i][0]
  elif s[i] == 5:
   s[i] = 2+c[i][0]
  elif s[i] == 6:
   s[i] = 4+c[i][0]
  else :
   s[i] = c[i][0]
 m = max(s)
 if s.count(m) > 1:
  print('tie')
 else:
  j = s.index(m)
  if j == 0:
   print('chef')
  else :
   print(j+1)

