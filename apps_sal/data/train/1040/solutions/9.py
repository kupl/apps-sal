for _ in range(int(input())):
 N,Q=map(int,input().split())
 S=input()
 Z=[0 for x in range(N)]
 LC=0
 for I in range(2,N):
  if S[I-2]==S[I-1] or S[I-2]==S[I] or S[I-1]==S[I]:
   LC+=1
  Z[I]=LC
 for I in range(Q):
  L,R=map(int,input().split())
  F=0
  if R-L<2:
   print('NO')
  else:
   if Z[R-1]==Z[L]:
    print('NO')
   else:
    print('YES')
