# cook your dish here
t=int(input())
while t>0:
 s=list(input())
 l=len(s)
 for i in range(l):
  if s[i]=='m' and i>0 and s[i-1]=='s':
   s[i-1]='*'
  elif s[i]=='m' and i<l-1 and s[i+1]=='s':
   s[i+1]='*'
 c=s.count('s')
 d=s.count('m')
 if c>d:
  print("snakes")
 elif d>c:
  print("mongooses")
 else:
  print("tie")
 t-=1
