t = int(input())
for _i in range(t):
 n = int(input())
 words = input().split()
 
 words = sorted(words, key=lambda x: len(x))
 mw = words[0]
 words = words[1:]
 
 ans,alen = '',0
 for i in range(len(mw)):
  for j in range(i,len(mw)):
   ss = mw[i:j+1]
   
   found = True 
   for word in words:
    if ss not in word:
     found = False
     break
   
   if found:
    if len(ss) > alen:
     ans,alen = ss,len(ss)
    elif len(ss) == alen and ss < ans:
     ans,alen = ss,len(ss)
 
 print(ans)

