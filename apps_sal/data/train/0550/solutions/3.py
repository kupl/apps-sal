t = int(input())
while(t):
 a, b = map(int ,input().split())
 stra = bin(a).replace("0b", "")
 strb = bin(b).replace("0b","")
 if(len(stra) == len(strb)):
  pass
 elif(len(stra) > len(strb)):
  addi = len(stra) - len(strb)
  for i in range(addi):
   strb = '0' + strb
 else:
  addi = len(strb) - len(stra)
  for i in range(addi):
   stra = '0'+ stra
 n = len(strb)
 maxi = int(stra, 2) ^ int(strb, 2)
 i = 0
 indi = 0
 tem = strb[-1] + strb[0:n-1]
 while(tem != strb):
  c = int(stra, 2) ^ int(tem, 2)
  i += 1
  if(c >= maxi):
   maxi = c
   indi = i
  tem = tem[-1] + tem[0:n-1]
 print(indi, maxi)
 t = t - 1
