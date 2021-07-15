for _ in range(int(input())):
 N,K=map(int,input().split())
 seq=[int(i) for i in input().split()]
 value=0
 turn=0
 for i in range(N):
  if(seq[i]==0):
   value+=seq[i]
   turn=int(not(turn))
  else:
   if(turn==0):    #vanja's turn
    if(K - abs(value + 1) <= K - abs(value-1)):
     value+=1
     turn=1
    else:
     value-=1
     turn=1
   else:           #miksi's turn
    if(K - abs(value + 1) <= K - abs(value-1)):
     value-=1
     turn=0
    else:
     value+=1
     turn=0
 if(abs(value) >= K):
  print(1)
 else:
  print(2)
