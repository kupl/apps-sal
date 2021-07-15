for _ in range(int(input())):
 s=input()
 p=int(len(s))
 r=list(s)
 w=0
 if r==r[::-1]:
  print('YES')
 else:
  for i in range(p):
   w=2
   r.pop(i)
   if r==r[::-1]:
    w=1
    break
   r=list(s)
 if w==1:
  print("YES")
 elif w==2:
  print("NO") 

