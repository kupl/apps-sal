def scorec(x,y):
  if x==y and x>0:
    score=2*x-1
  elif x==y and x<0:
    score=2*abs(x)
  else:
    if y+x>0:
      score=2*max(abs(x),abs(y))-2
    else:
      score=2*max(abs(x),abs(y))-1
  return max(0,score)
t=int(input())

for _ in range(t):
  ax,ay,bx,by,cx,cy=list(map(int,input().split()))
  overlap=0
  ans1=scorec(ax,ay)
  if ans1<=0:
    overlap+=1
  ans2=scorec(bx,by)
  if ans2<=0:
    overlap+=1
  ans3=scorec(cx,cy)
  if ans3<=0:
    overlap+=1
  ans=min(ans1,ans2,ans3)
  if overlap>=2:
    print((3-overlap))
    continue
  if (ans+2==ans1 and ans+2==ans2) or (ans+2==ans2 and ans+2==ans3) or (ans+2==ans1 and ans+2==ans3):
    ans+=1
  print((ans+2))

