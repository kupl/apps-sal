for _ in range(int(input())):
 n=int(input())
 a=list(map(int, input().split()))
 xorsum=[]
 xor=0
 xorsum.append(xor)
 for i in range(len(a)):
  xor^=a[i]
  xorsum.append(xor)
  
 xordict=dict()
 for i in range(len(xorsum)):
  if xorsum[i] in xordict:
   xordict[xorsum[i]].append(i)
  else:
   xordict[xorsum[i]] = [i]
 ans=0
 for key in xordict:
  for i in range(1,len(xordict[key])):
   x=(i*xordict[key][i])-(i)-(sum(xordict[key][:i]))
   ans+=x
 print(ans)
