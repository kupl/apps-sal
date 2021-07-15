# cook your dish here
for _ in range(int(input())):
 N,K=map(int,input().split(' '))
 S=input()
 
 S=S.replace('H','1').replace('T','0').replace(' ','')
 # print(S)
 for i in range(1,K+1):
  currBit=S[N-i]
  S=S[:-1]
  if(currBit=='0'):
   continue
  else:
   S_dec=int(S,2)
   xor_mulp=2**(N-i+1)-1
   S=bin(S_dec^xor_mulp)[3:]
 # print(S)
 print(sum(map(int,list(S))))
