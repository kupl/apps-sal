day = 1
d1,v1,d2,v2,p = map(int,input().split())
d1 = abs(d1)
v1 = abs(v1)
d2 = abs(d2)
v2 = abs(v2)
p = abs(p)
vaccines = 0
while(1):
 if(day >= d1):
  vaccines += v1
 if(day >= d2):
  vaccines += v2
 if(vaccines >= p):
  break
 day += 1
print(day)
