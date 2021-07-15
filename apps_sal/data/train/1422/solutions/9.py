t = int(input())
for nTest in range(t):
 n = int(input())
 s = list(input().strip())
 answer = 0
 for i in range(n):
  if (i==0 or s[i-1]=='0') and (s[i]=='0') and (i==n-1 or s[i+1]=='0'):
   answer +=1
 print(answer)

