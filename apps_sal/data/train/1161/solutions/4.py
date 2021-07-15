# cook your dish here
for i in range(int(input())):
 a=str(input())
 s=a.count('s')
 m=a.count('m')
 j=0
 while j<len(a)-1:
  if a[j]=='s' and a[j+1]=='m' or a[j]=='m' and a[j+1]=='s':
   j+=2
   s-=1
  else:
   j+=1
 if s>m:
  print("snakes")
 elif m>s:
  print("mongooses")
 else:
  print("tie")
