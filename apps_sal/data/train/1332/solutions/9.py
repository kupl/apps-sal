N=eval(input())
while N:
 N-=1
 a,b=[int(x) for x in input().split()]
 count=0
 a=bin(a)[2:]
 b=bin(b)[2:]
 j=0
 for i in range(0,min(len(a),len(b))):
  if a[i]==b[i]:
   j=i
   continue
  else:
   count+=(len(a)-i)
   count+=(len(b)-i)
   break
 if j==min(len(a),len(b))-1:
  count+=(len(a)+len(b)-2*j-2)
 print(count)
 

