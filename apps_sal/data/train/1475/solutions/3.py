# your code goes here
from sys import stdin, stdout
s = stdin.readline().strip().split(' ')
k = stdin.readline().strip()
for i in k:
 countk = list(k)
 countk.sort()
 countk = "".join(countk)
ans = ""
for i in range(len(s)):
 if s[i] != k:
  counti = list(s[i])
  counti.sort()
  counti = "".join(counti)
  if counti == countk:
   ans += str(i+1)
stdout.write("The antidote is found in "+ans+".")
