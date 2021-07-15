# cook your dish here
import math
for _ in range(int(input())):
 N, D = list(map(int, input().split(' ')))
 lst = list(map(int, input().split(' ')))
 if D==1:
  print(N)
 else:
  lst1=[]
  lst2=[]
  for ele in lst:
   if ele<=9 or ele>=80:
    lst1.append(ele)
   else:
    lst2.append(ele)
  x=math.ceil(len(lst1)/D)
  y=math.ceil(len(lst2)/D)
  print(x+y)
    

