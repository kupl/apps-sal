from collections import Counter
t = 0
try:
 t = int(input())
except:
 pass
for _ in range(t):
 n = int(input())
 s = input()
 s = s[:n]
 c = Counter(s)
 sums = 0
 sums += min(c['D'],c['U'])
 sums += min(c['L'],c['R'])
 print(sums*2)
