s = input()
result = [""] * len(s)
l = 0; r = len(s) - 1
for i in range(len(s)):
  if s[i] == 'r':
    result[l] = str(i+1)
    l += 1
  else:
    result[r] = str(i+1)
    r -= 1
from sys import stdout
stdout.write('\n'.join(result))
