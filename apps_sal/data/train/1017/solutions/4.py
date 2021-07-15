# cook your dish here
t = int(input())
for z in range(t) :
 a = [int(x) for x in input().split()]
 p = a[-1]
 a = a[:-1]
 s = 0
 for i in a:
  s+= i*p 
 if s>120 :
  print("Yes")
 else:
  print('No')
