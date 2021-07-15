for _ in range(int(input())):
 n, k, x, y = list(map(int, input().strip().split()))
 direc = "upright"
 for i in range(k):
  if direc == "upright":
   if y>x:
    x += n - y
    y = n
    direc = "downright"
   else:
    y += n - x
    x = n
    direc = "upleft"
  elif direc== "downleft":
   if y > x:
    y -= x
    x = 0
    direc = "downright"
   else:
    x -= y
    y = 0
    direc = "upleft"
   # while x!=0 or y!=0:
   #     x-=1
   #     y-=1
   # if x == 0:
   #     direc = "downright"
   # else:
   #     direc = "upleft"
  elif direc == "upleft":
   if x+y < n:
    y += x
    x = 0
    direc = "upright"
   else:
    x -= n-y
    y = n
    direc = "downleft"
  elif direc == "downright":
   if x+y < n:
    x += y
    y = 0
    direc = "upright"
   else:
    y -= n - x
    x = n
    direc = "downleft"
   # while y!=0 or x!=n:
   #     x+=1
   #     y-=1
   # if y == 0:
   #     direc = "upright"
   # else:
   #     direc = "downleft"
  if [x, y] in [[0,0], [0,n], [n,0], [n,n]]:
   break
 print(x, y)

