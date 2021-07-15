t = int(input())
for t1 in range(t):
 h, m = input().split(":")
 h, m = int(h), int(m)
 
 h = h%12
 
 h = 30*h + m/2
 am = m*6;
 ans = min(abs(h - am), 360 - abs(am - h))
 if ans - int(ans) == 0:
  print(str(int(ans)) + " degree")
 else:
  print(str(ans) + " degree")
