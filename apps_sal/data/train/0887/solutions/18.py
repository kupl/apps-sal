

t = int(input())

for m in range(t):

 n = int(input())
 l1 = list(map(int,input().split()))
 l2 = list(map(int,input().split()))
 flag = 0
 if l1[0]!=0 or l1[-1] == 0 or l2[0] == 0 or l2[-1]!=0 or l1[-1]!=l2[0]:
  flag = 1

 if flag!=1:
  for i in range(1,n-1):
   if l1[i]+l2[i]<l1[-1]:
    flag = 1
    break
   if l1[-1]+l2[i]<l1[i]:
    flag = 1
    break
   if l1[-1]+l1[i]<l2[i]:
    flag = 1
    break
 if flag == 0:
  print('Yes')
 else:
  print('No')
