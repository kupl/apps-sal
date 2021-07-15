# cook your dish here
t = int(input())

for _ in range(t):
 n = int(input())
 s = input()
 l = []
 for i in range(n):
  yo = s[:i] + s[i+1:]
  for j in range(n):
   k1 = yo[:j] + s[i] + yo[j:]
   l.append(k1)
 l.sort()
 print(l[0])

