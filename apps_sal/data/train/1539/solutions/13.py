#Jewels And Stones
def common(s1,s2):
 n=0
 done=[]
 for i in s1:
  if i in done:
    continue
  for j in s2:
   if i==j:
    n+=1
  done+=[i]
 return n
t=int(input())
for i in range(t):
 s1=str(input())
 s2=str(input())
 print(common(s1,s2))

