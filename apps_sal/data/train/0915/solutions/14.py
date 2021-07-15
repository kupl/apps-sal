t =int(input())
for i in range(t):
 n = int(input())
 li = list(map(int, input().split()))[:n]
 a = []
 for i in li:
  if li.count(i) == 1:
   a.append(i)
  if i not in a:
   a.append(i)
 print(len(a))

