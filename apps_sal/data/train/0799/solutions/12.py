res=0
for _ in range(int(input())):
 x=list(map(int,input().split()))
 if x.count(1)>=2:
  res+=1
print(res) 
