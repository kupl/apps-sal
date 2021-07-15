count=0
n=int(input())
for i in range(n):
 p_1=list(map(int,input().split()))
 if((p_1.count(1)>1)):
  count=count+1
print(count)
