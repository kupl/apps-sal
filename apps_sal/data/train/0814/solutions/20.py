# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 s = input().split()
 s = "".join(s).split('1')
 l = []
 for i in s:
  if len(i):
   l.append(i)
 l.sort(reverse = True, key = len)
 if len(l) == 0:
  print("No")
 else:
  if len(l) == 1:
   if len(l[0])%2!=0:
    print("Yes")
   else:
    print('No')
  else:
   m1,m2 = len(l[0]), len(l[1])
   if m1%2 == 0:
    print("No")
   else:
    if (m1+1)//2>m2:
     print("No")
    else:
     print("Yes")

