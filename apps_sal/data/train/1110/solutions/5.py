for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    dli=dict()
    modi=0
    #2*n optimiztion 
    for i in li:
     if i not in dli:
      dli[i]=li.count(i)
    if(len(dli)!=0):
     while 1:
      tmp=[]
      for i in dli:
       if dli[i]==0:
        continue
       tmp.append(i)
       dli[i]-=1
      l=len(tmp)
      mn=l
      for i in range(l):
       mn=min(mn,tmp[i]-1-i+l-1-i)
      modi+=mn
      if(l==0):
       break
    print(modi)
