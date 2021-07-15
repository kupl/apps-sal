for t in range(int(input())):
 n = int(input())
 mx = -1
 for i in range(n):
  h, m, s = list(map(int,input().split(":")))
  h %= 12
  m %= 60
  s %= 60
  ha = h*30 + m*0.5 + s*0.5/60
  ma = m*6 + s*0.1
  sa = s*6
  
  hm1 = abs(ha - ma)
  hm2 = 360 - hm1
  hm3 = abs(hm1 - hm2)
  hm = min(hm1, hm2, hm3)
  
  ms1 = abs(ma - sa)
  ms2 = 360 - ms1
  ms3 = abs(ms1 - ms2)
  ms = min(ms1, ms2, ms3)
  
  sh1 = abs(sa - ha)
  sh2 = 360 - sh1
  sh3 = abs(sh1 - sh2)
  sh = min(sh1, sh2, sh3)
  
  avg = (hm + ms + sh) / 3
  if (mx < avg):
   ans = i+1
   mx = avg
 print(ans)
