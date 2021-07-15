# cook your dish here
try:
 for t in range(int(input())):
  n = int(input())
  a = list(map(int, input().split(' ')))
  s = min(a)
  a.remove(s)
  ss = min(a)
  print(s + ss)
except:
 pass
