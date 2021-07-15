for _ in range(int(input())):
 n=int(input())
 l=[]
 while n>0:
  k=[]
  k=[int(i) for i in input().split()]
  k=sorted(k)
  l.append(k)
  n -= 1

 count = [l[-1][-1]]
 flag = 0
 for i in range(len(l)-2,-1,-1):
  for j in range(len(l)-1,-1,-1):
   if l[i][j]< count[-1]:
    count.append(l[i][j])
    break
  else:
   flag = 1
   break
  if flag == 1: break
 if flag == 1: print(-1)
 else: print(sum(count))






