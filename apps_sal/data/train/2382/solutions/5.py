def check(a, b):
  dif = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      dif += 1
      if dif == 2:
        return False
  return True

for _ in range(int(input())):
  n, m = map(int, input().split())
  data = []
  for i in range(n):
    data.append(input())

  result = False
  for i in range(m):
    for j in range(0, 26):
      now = data[0][:i] + chr(ord('a') + j) + data[0][i + 1:]
      temp = True
      for k in data[1:]:
        if not check(now, k):
          temp = False
      if temp:
        print(now)
        result = True
        break
    if result:
      break
  
  if not result:
    print("-1")
