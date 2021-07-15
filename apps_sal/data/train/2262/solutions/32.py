def main(r,c,n,xy):
  ary=[]
  for i,(x1,y1,x2,y2) in enumerate(xy):
    if x1 in (0,r) or y1 in (0,c):
      if x2 in (0,r) or y2 in (0,c):
        for x,y in ((x1,y1),(x2,y2)):
          tmp=0
          if x==0:
            tmp=y
          elif x==r:
            tmp=r+c+(c-y)
          elif y==0:
            tmp=2*r+2*c-x
          elif y==c:
            tmp=c+x
          ary.append([i,tmp])
  ary.sort(key=lambda x:x[1])
  #print(ary)
  stc=[]
  for i,x in ary:
    if stc and stc[-1]==i:
      stc.pop()
    else:
      stc.append(i)
  if stc:
    return 'NO'
  else:
    return 'YES'

def __starting_point():
  r,c,n=map(int,input().split())
  xy=[list(map(int,input().split())) for _ in range(n)]
  print(main(r,c,n,xy))
__starting_point()
