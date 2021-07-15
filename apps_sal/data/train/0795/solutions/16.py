# cook your dish here
for _ in range(int(input())):
 N,K,L=(int(i) for i in input().split(' '))
 if(((N/K)>L) or (K==1 and N!=K)):
  print(-1)
 else:
  noOfSessions=(N//K)+1
  bowlerLst=list(range(1,K+1))
  totalOvers=(bowlerLst*noOfSessions)[:N]
  print(*totalOvers)

