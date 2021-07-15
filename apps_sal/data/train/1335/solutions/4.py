n=int(input())
lis=list(map(int,input().split()))
dic={}
for i in lis:
 if i in dic:
  dic[i]+=1
 else:
  dic[i]=1
cnt=0
for i in dic:
 while dic[i]>=2:
  dic[i]-=2
  cnt+=1
 if dic[i]!=0:
  cnt+=1
print(cnt)
