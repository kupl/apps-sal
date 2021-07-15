for t in range(int(input())):
 n,c = map(int,input().split())
 E =[]
 dic = {}
 for i in range(n):
  x,y = map(int,input().split())
  E.append([x,y])
  dic[x-y] = []

 

 for i in E:
  dic[i[0]-i[1]].append([i[0],i[1]])

 count = 0
 moves = 0
 for i in dic:
  sub = {}
  for j in dic[i]:
   x,y = j[0],j[1]
   if sub.get(x%c,-1)==-1: 
    sub[x%c] = [[x,y]]
   else:
    sub[x%c].append([x,y])

  count += len(sub)

  for j in sub:
   arr = sorted(sub[j])
   m1 = arr[len(arr)//2][0]
   for k in arr:
    moves += abs(k[0]-m1)//c
 print(count,moves)
