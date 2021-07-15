for _ in range(int(input())):
 l=list(input())
 temp=['<','=']
 fg,c=0,0
 ans1,ans2=0,0
 for i in range(len(l)):
  if l[i] in temp:
   fg=1
   if l[i]=='<':
    c+=1
  elif fg==1:
   ans1=max(ans1,c)
   fg=0
   c=0
 if fg==1:
  ans1 = max(ans1, c)
 ans1+=1
 temp=['>','=']
 fg,c=0,0
 for i in range(len(l)):
  if l[i] in temp:
   fg=1
   if l[i]=='>':
    c+=1
  elif fg==1:
   ans2=max(ans2,c)
   fg=0
   c=0
 if fg==1:
  ans2 = max(ans2, c)
 ans2+=1
 print(max(ans1,ans2))
