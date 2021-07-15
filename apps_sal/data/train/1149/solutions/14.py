test = int(input())
for _ in range(test):
 string=list(input())
 answer=1
 for i in range(len(string)//2):
  if string[i]=='?' and string[len(string)-i-1]=='?':
   answer = (answer*26)%10000009
  elif string[i]=='?' or string[len(string)-i-1]=='?':
   answer=(answer*1)
  elif string[i]!=string[len(string)-i-1]:
   answer=0
   break
 if len(string)%2!=0:
  if string[len(string)//2]=='?':
   answer=(answer*26)
 print(answer%10000009)
