s = input()
n = len(s)

if s[0] != "1" or s[n - 1] != "0":
  print("-1")
  return

for i in range(n):
  if s[i] != s[n - 2 - i]:
    print("-1")
    return

x = 1
for i in range(1, n):
  print(x, i + 1)
  if s[i - 1] == "1": x = i + 1
