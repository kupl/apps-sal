for _ in range(int(input())):
 h,m = tuple(map(int, input().split(":")))
 #a = list(map(int, input().split()))
 if m % 5 != 0:
  m = m + (5 - m %5)
 anm = int(360 * (m/60))%360
 h = h % 12
 anh = h * 30 + 30 * (m/60)
 ans = abs(anh-anm) if abs(anh-anm) <= 180 else 360 - abs(anh-anm)
 if ans == int(ans):
  ans = int(ans)
 print(ans,"degree")
 

