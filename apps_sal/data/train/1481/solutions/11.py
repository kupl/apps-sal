# cook your dish here
for _ in range(int(input())):
 s = input()
 lisS = list(s)
 
 if(len(set(lisS))==1 or len(s) % 2 != 0):
  print(-1)
 else:
  mid = len(s) // 2
  numZeros = 0
  for i in range(len(s)):
   if(s[i] == "0"):
    numZeros += 1
  
  print(abs(mid - numZeros))
