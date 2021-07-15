def __starting_point():
 n,m,p = list(map(int, input().split()))
 hit={}
 sums={}
 for i in range(1,n+1):
  hit[i]={}
  sums[i]=m-1
 for _ in range(p):
  i,j = list(map(int, input().split()))
  if j not in hit[i]:
   hit[i][j]=1
  else:
   hit[i][j]+=1
 for i in range(1,n+1):
  done = True
  for j in hit[i]:
   if j!=m and (hit[i][j] - hit[i].get(j+1,0)) > 1:
    done=False
    break
   if j==1 and m>1: sums[i]-=hit[i][j]
   elif j==m and m>1: sums[i]+=hit[i][j]
  if done:
   print(sums[i])
  else:
   print(-1)
 
  

__starting_point()
