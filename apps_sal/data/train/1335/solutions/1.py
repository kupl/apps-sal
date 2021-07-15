# cook your dish here
n = int(input())
a = list(map(int,input().split()))
v = dict()
count = 0
for i in range(n):
 k = a[i]
 if k in v:
  v[k] += 1
 else:
  v[k] = 1
for x in v:
 if v[x] >= 2 :
  if v[x] % 2 == 0:
   count += v[x] // 2
  else:
   count += v[x] // 2
   count += 1
 else:
  if v[x] == 1:
   count += 1
  
print(count) 
