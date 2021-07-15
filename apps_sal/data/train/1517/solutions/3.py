t=int(input())
for tc in range(0,t):
 n,k=list(map(int,input().split()))
 num=list(map(int,input().split()))
 den=list(map(int,input().split()))
 temp=n
 for i in range(0,k):
  temp=temp+(temp**1.0*num[i]/den[i])
 answer=int(100-(n*1.0*100/temp))
 print(answer)
