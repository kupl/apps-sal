from sys import stdin
a = stdin.readlines()
for i in a:
 b = list(i.strip())
 ans = 'Invalid'
 if len(b)==len(set(b)):
  ans = 'Valid'
  print(ans)
  break
 print(ans)
