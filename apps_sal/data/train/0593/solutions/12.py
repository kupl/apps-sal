import bisect
from collections import Counter
for _ in range(int(input())):
 a=list(map(int,input().split()))
 s=input()
 c=0
 for i in range(ord('a'),ord('z')+1):
  if chr(i) not in s:
   c+=a[i-97]
 print(c)

