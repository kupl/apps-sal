t = int(input())
for _ in range(t):
  ax,ay,bx,by,cx,cy = map(int,input().split())
  mnx = min(ax,bx,cx)
  mny = min(ay,by,cy)
  tp = ((ax,ay),(bx,by),(cx,cy))
  ans = 0
  if (mnx+1,mny+1) not in tp:
    if mnx == mny and mnx != 0:
      ans += 1
    ans += max(abs(mnx),abs(mny))*2
    print(ans)
  elif (mnx+1,mny) not in tp:
    mnx = abs(mnx)
    if mny < 0:
      mny = abs(mny+1)
    if mnx > mny:
      print(mnx*2)
    else:
      print(mny*2+1)
  elif (mnx,mny+1) not in tp:
    mny = abs(mny)
    if mnx < 0:
      mnx = abs(mnx+1)
    if mny > mnx:
      print(mny*2)
    else:
      print(mnx*2+1)
  else:
    ans += 1
    if mnx == mny and mnx != 0:
      ans += 1
    if mnx < 0:
      mnx = abs(mnx+1)
    if mny < 0:
      mny = abs(mny+1)
    ans += max(abs(mnx),abs(mny))*2
    print(ans)
