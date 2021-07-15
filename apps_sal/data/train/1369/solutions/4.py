def sieve(x):
 p = [1]*(x+1)
 p[0] = 0
 p[1] = 0
 
 t = 2
 while(t**2 < x):
  if p[t] == 1:
   for j in range(t**2, x+1, t):
    p[j] = 0
  t += 1
 
 return p

l = sieve(10**6 +2)
s = [0]

for i in range(1, len(l)):
 if l[i] == 1:
  s.append(s[i-1] + i)
 else:
  s.append(s[i-1])


for u in range(int(input())):
 x = int(input())
 print(s[x])
