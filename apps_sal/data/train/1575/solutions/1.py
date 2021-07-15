import sys

for __ in range(eval(input())) :
 m , n , o = eval(input()) , eval(input()) , eval(input())
 if m==1 and n==1 and o==1 :
  print(0)
  continue
 print((m-2)*4+(n-2)*4+(o-2)*4)

