N,M,K=list(map(int,input().split()))
c=0
for i in range(N):
 T=list(map(int,input().split()))
 Q=T[-1]
 T.pop(-1)
 if Q<=10 and sum(T)>=M:
  c+=1
print(c)

