a = 0
ans = None
for t in range(int(input())):
 j, d = list(map(int,input().split()))
 a+=j
 a-=d
 if (ans is None):
  ans = t
 if (a <= 0):
  a = 0
  ans = None
if (ans is None):
 print(0)
else:
 print(ans)
