case = int(input())
for i in range(0, case):
 try:
  l = [elem for elem in input().split()]
  res = int(l[0][::-1]) + int(l[1][::-1])
  print(int(str(res)[::-1]))
 except:
  break
