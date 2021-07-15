T=int(input())
for _ in range(T):
    A,B=list(map(int,input().split()))
    cs=list(map(int,input().split()))
    ds=list(map(int,input().split()))
 
    for i in range(A*B):
     if cs[i]<ds[i]:
      cs[i]=0
     else:
      ds[i]=0

    cs.sort(reverse=True)
    ds.sort(reverse=True)

    w,c,d=0,0,0
    for _ in range(A):
     if cs[c]>ds[d]:
      w+=1
      c+=1
      d+=B-1
     else:
      d+=B
   
    print(w)

