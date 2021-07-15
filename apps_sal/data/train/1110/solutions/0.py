# cook your dish here
for _ in range(int(input())):
    n=int(input());li=list(map(int,input().split()));dli=dict();modi=0
    for i in li:
     if i not in dli:dli[i]=1
     else:dli[i]+=1
    op=sorted(list(dli))
    if(len(dli)!=0):
     while 1:
      tmp=[]
      for i in op:
       if dli[i]==0:continue
       tmp.append(i);dli[i]-=1
      l=len(tmp);mn=l
      for i in range(l):mn=min(mn,tmp[i]-1-i+l-1-i)
      modi+=mn
      if(l==0):break
    print(modi)
