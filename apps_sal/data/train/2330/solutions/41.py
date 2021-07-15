s = input()
if s[-1] == "1":
  print(-1)
  return
s = s[:-1]
if s != s[::-1] or s[0] == "0":
  print(-1)
  return
s += "1"
n = len(s)
now = 1
for i, t in enumerate(s, 1):
  if t == "1":
    for j in range(now, i):
      print(j, i)
      now = i
