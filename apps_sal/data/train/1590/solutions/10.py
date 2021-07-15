for i in range(int(input())):
 li=list(map(int,input().split()))
 '''if a>0 and b>0 and c>0:
     if a+b>c or b+c>a or a+c>b :
      print("Yes")
     else:
      print("No")
    else:
     print("No")'''
 a=max(li)
 b=min(li)
 c=0
 for j in li:
  if j!=a and j!=b:
   c=j
   break
 if c==0:
  if li.count(min(li))>li.count(max(li)):
   c=min(li)
  else:
   c=max(li)
 if b+c>=a-1:
  print("Yes")
 elif a==b and a==c:
  print("Yes")
 else:
  print("No")

