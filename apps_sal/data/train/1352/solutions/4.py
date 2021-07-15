t=int(input().strip())
for test in range(t):
 n=int(input().strip())
 word=list(map(int,input().strip().split(" ")))
 word=sorted(word)
 i=0
 ab=[]
 while(i<len(word)):
  if word[i] not in ab:
   ab.append(word[i])
   print(str(word[i])+": "+str(word.count(word[i])))
  i=i+1
 

