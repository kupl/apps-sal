# cook your dish here
from collections import deque
for _ in range(int(input())):

 n, k = list(map(int, input().split()))
 s = input()

 new_s = ""
 for obj in s:
  if obj == ":":
   new_s+=obj
  new_s+=obj

 qi = deque()
 qm = deque()

 ans = 0; j = 0
 for i in new_s:

  if i == 'I':
   while (len(qm)!=0 and qm[0]+k < j):
    qm.popleft()

   if len(qm) != 0:
    ans+=1
    qm.popleft()

   else:
    qi.append(j)

  elif i == 'M':
   while (len(qi) != 0 and qi[0]+k < j):
    qi.popleft()

   if len(qi)!=0:
    ans+=1
    qi.popleft()

   else:
    qm.append(j)

  elif i == 'X':
   while len(qm)!=0:
    qm.popleft()
   while len(qi)!=0:
    qi.popleft()

  j+=1
 print(ans)

