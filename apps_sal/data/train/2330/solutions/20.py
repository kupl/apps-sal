import sys

s = input()
N = len(s)
if s[-1] == "1" or s[0] == "0":
  print((-1)); return
  
for i in range(N//2):
  if s[i] != s[-i-2]:
    print((-1)); return

tmp = 1
for i in range(N-1):
  print((tmp, i+2))
  if s[i] == "1":
    tmp = i+2

