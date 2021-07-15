for _ in range(int(input())):
 n, m = map(int, input().split())
 s = input()
 ans = 'unsafe'

 for i in range(n):
  for j in range(m):
   x, y = i, j
   res = 1
   for k in s:
    if k == 'L':
     y -= 1
    elif k == 'U':
     x -= 1
    elif k == 'R':
     y += 1
    else:
     x += 1
    if x < 0 or x >= n or y < 0 or y >= m:
     res = 0
     break

   if res:
    ans = 'safe'
    break 
 print(ans)
