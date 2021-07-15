T=int(input())
for i in range(T):
 N=int(input())
 C=0
 for j in range(N):
  F=0
  P,Q,D=list(map(int,input().split()))
  F=P+(P*(D/100))
  F=F-(F*(D/100))
  C+=((P-F)*Q)
 print(C)

