cases = int(input())

for case in range(cases):
 N, M, K = [int(i) for i in input().split()]
 A = [int(i) for i in input().split()]
 jad = 0
 P = M*K

 for milk in A:
  if(milk>P):
   jad += milk-P
  else:
   jad += milk%K

 print(jad%1000000007)

