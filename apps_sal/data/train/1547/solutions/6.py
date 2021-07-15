
d1,v1,d2,v2,vaccine = map(int,input().split())
day = 1
sum = 0
while sum<vaccine:
 if day==d1:
  sum+=v1
  d1+=1 
 if day==d2:
  sum+=v2
  d2+=1
 if sum>=vaccine:
  break
 day+=1
print(day)
