t=int(input())
MOD=(10**9)+7
l=['a','e','i','o','u']
for i in range(t):
 s=input()
 k=[]
 for j in s:
  if j in l:
   k.append(1)
  else:
   k.append(0)
 r=bin(int(''.join(map(str, k)), 2) << 1)
 print((int(r,2)//2)%MOD)

