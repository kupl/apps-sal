n,a=list(map(int,input().split()))
n=list(map(int,str(n)))
for i in range(a):
 if(n[-1]==0):
  n.pop()
 else:
  n[-1]-=1
 if(len(n)==0):
  break
if(len(n)==1):
 print(int(n[0]))
elif(len(n)==0):
 print(0)
else:
 n=list(map(str,n))
 print(int("".join(n)))

