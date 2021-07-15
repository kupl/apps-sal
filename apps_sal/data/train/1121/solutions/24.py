
for _ in range(int(input())):
 l=input().split(":")
 hr=int(l[0])%12
 mi=int(l[1])
 hour_angle = (hr % 12) * 30 + mi * 0.5
 minute_angle = mi * 6
 ans = abs(hour_angle - minute_angle)
 if ans%1==0:
  print(min(int(ans), 360 - int(ans)), "degree")
 else:
  print(min(ans,360-ans)," degree")


