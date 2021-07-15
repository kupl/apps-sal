T = int(input())

while T>0:
 n = int(input())
 words = input().split()
 words.sort(key = lambda s: len(s))
 temp = words[0]
 l = len(temp)
 
 ans = []
 for i in range(0,l+1):
  ans = []
  for j in range(0,i+1):
   t = temp[j:l-i+j]
   check = True
   for k in range(1,n):
    if t in words[k]:
     continue
    else :
     check =False
     break
   if check:
    ans.append(t)
  
  if len(ans)>0:
   break
 
 ans.sort()
 print(ans[0])
 
 T =T-1
