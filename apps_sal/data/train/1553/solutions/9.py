while True:
 try:
  rolcol = input().split()
  row = int(rolcol[0])
  col = int(rolcol[1])
  tree = []
  for i in range(row):
   a = input().split()
   tree.append(a)
  sell = int(input())
  for i in range(sell):
   sum1 = 0
   pos = input().split()
   x1 = int(pos[0])-1
   y1 = int(pos[1])-1
   x2 = int(pos[2])-1
   y2 = int(pos[3])-1
   for j in range(x1,x2+1):
    for k in range(y1,y2+1):
     sum1 = sum1 + int(tree[j][k])
   print(sum1) 
 except EOFError:
  break
