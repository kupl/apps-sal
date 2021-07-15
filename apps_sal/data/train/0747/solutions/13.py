from collections import Counter
for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 b = []
 c = []
 for i in a:
  if i in b:
   c.append(i)
  else:
   b.append(i)
 b.sort()
 c.sort(reverse=True)
 flag = 0
 d = Counter(c)
 for i in d.values():
  if i > 1 or c[0] == b[-1]:
   flag = 1
   print("NO")
   break
 if flag == 0:
  print("YES")
  b.extend(c)
  print(*b)
