# cook your dish here
from operator import itemgetter
for _ in range(int(input())):
 n=int(input())
 info=[]
 val=0
 for i in range(n):
  lst=list(input().strip().split())
  val+=int(lst[2])
  info.append(lst)
 info.sort(key=lambda info:info[2])
 #print(ans)
 final=[]
 val=val/n
 for i in range(n):
  if int(info[i][2])<val:
   final.append(info[i])
 
 for i in final:
  print(i[0],i[1],i[2])
