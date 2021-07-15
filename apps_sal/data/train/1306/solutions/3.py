# cook your dish here
from collections import Counter
for _ in range(int(input())):
 
 c=Counter(input())
 #LTIME
 if c['L']>=2 and c['T']>=2 and c['I']>=2 and c['M']>=2 and c['E']>=1:
  print('YES')
 else:
  print('NO')
  

