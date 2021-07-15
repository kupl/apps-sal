for i in range(int(input())):
 m, n = map(int, input().split())
 rx, ry = map(int, input().split())
 num = int(input())
 s = input()
 x = 0
 y = 0
 for j in s:
  if(j=='U'):
   y=y+1
  elif(j=='D'):
   y=y-1
  elif(j=='R'):
   x=x+1
  elif(j=='L'):
   x=x-1
 if x == rx and y == ry:
  print("Case "+str(i+1)+": REACHED")
 elif x != rx and y != ry and x > 0 and x <= m and y > 0 and y <= n:
  print("Case "+str(i+1)+": SOMEWHERE")
 elif x < 0 or x > m or y < 0 or y > n:
  print("Case "+str(i+1)+": DANGER")
