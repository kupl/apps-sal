p, s = list(map(int, input().split()))
sub = []
pro = []
t = []
for i in range(p):
 sub.append(list(map(int, input().split())))
 pro.append(list(map(int, input().split())))
for i in range(p):
 t.append(list(zip(sub[i], pro[i])))
indices = []

for a in t:
 a.sort(key = lambda x: x[0])
 m = 0
 n = 0
 while m != s-1:
  if a[m][1] > a[m+1][1]:
   n += 1
  m += 1
 indices.append(n) 

pb = [i+1 for i in range(p)]
sol = list(zip(indices, pb))
sol.sort()
for a in sol:
 print(a[1])










