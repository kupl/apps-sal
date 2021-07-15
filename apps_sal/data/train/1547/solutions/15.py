try:
 a=list(map(int,input().split()))
 d1=a[0]
 v1=a[1]
 d2=a[2]
 v2=a[3]
 p=a[4]
 vacc=0
 day=0
 if d1==d2:
  print(v2)
 else:
  for i in range(1,1000):
   if i>=d1:
    vacc=vacc+v1
   if i>=d2:
    vacc=vacc+v2
   day=day+1
   if vacc>=p:
    break
  print(day)
except:
 pass
