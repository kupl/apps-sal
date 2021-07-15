for _ in range(int(input())):
 l=list(map(str,input().split()))
 a=[(1,3,5),(1,3,6),(1,4,5),(1,4,6),(2,3,5),(2,3,6),(2,4,5),(2,4,6)]
 c=0
 for i in a:
  if len(set([l[i[0]-1],l[i[1]-1],l[i[2]-1]]))==1:
   c=1
   break
 if c==1:
  print("YES")
 else:
  print("NO")

