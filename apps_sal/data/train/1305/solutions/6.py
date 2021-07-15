res = []
for _ in range(int(input())):
 lst = []
 flag = 0
 n = int(input())
 for i in range(n):
  lst.append(list(map(int, input().split())))
 for i in lst:
  for j in range(n-1):
   if i[j] == i[j+1] == 1:
    res.append("UNSAFE")
    flag = 1
    break
  if flag != 0:
   break
 for i in range(n-1):
  for j in range(n):
   if lst[i][j] == lst[i+1] == 1:
    res.append("UNSAFE")
    flag = 1
    break
  if flag != 0:
   break
 if flag == 0:
  res.append("SAFE")
for i in res:
 print(i)

