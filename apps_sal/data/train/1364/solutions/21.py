from collections import defaultdict
t= int(input())
for _ in range(t):
 n,c = [int(x) for x in input().strip().split()]
 arr = defaultdict(list)
 for i in range(n):
  x,y = [int(z) for z in input().strip().split()]
  arr[x-y].append([x,y])
 cp = 0
 m = 0
 for i in arr:
  if len(arr[i]) == 1:
   cp+=1
  else:
   d = defaultdict(list)
   temparr = sorted(arr[i])
   d[0].append(temparr[0])
   for j in range(1,len(temparr)):
    d[(temparr[0][0]-temparr[j][0])%c].append(temparr[j])
   for j in d:
    cp+=1
    if len(d[j]) == 1:
     pass
    else:
     temparr = d[j]
     p = 0
     q = len(temparr)-1
     while p < q:
      m+=abs((temparr[p][0]-temparr[q][0])//c)
      p+=1
      q-=1
 print(cp,m)


  

