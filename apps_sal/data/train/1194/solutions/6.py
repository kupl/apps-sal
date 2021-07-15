from collections import Counter

x = int(input())
for i in range(0,x):
 len = int(input())
 string = str(input())
 dict = Counter(string)
 Ucount,Dcount,Lcount,Rcount = dict['U'],dict['D'],dict['L'],dict['R']
 ans = 0 
 if Ucount>0:
  if Dcount>0:
   y = abs(Ucount-Dcount)
   ans += Ucount+Dcount - y
 if Lcount>0:
  if Rcount>0:
   y = abs(Rcount-Lcount)
   ans += Rcount + Lcount - y 
 print(ans)





