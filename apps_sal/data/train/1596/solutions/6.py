t = int(input())
for _ in range(t):
 x,y = list(map(int,input().split()))
 x += 1
 y += 1
 ans1,ans2 = bin(x)[2:].count('1'),bin(y)[2:].count('1')
 if ans1 == ans2:
  print(0,0)
 elif ans1 > ans2:
  print(2,abs(ans1-ans2))
 else:
  print(1,abs(ans1-ans2))

