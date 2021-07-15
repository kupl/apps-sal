# cook your dish here
# cook your dish here
try:
 maxpoint=[]
 def maxpoints(n,string,sc):
  i=0
  points=0
  increaser=1
  while i<8:
   if string[i]=='.':
    points+=sc[i]
    i+=1
   elif string[i]=='d':
    points+=sc[i]*2
    i+=1
   elif string[i]=='t':
    points+=sc[i]*3
    i+=1
   elif string[i]=='D':
    increaser=increaser*2
    points+=sc[i]
    i+=1
   elif string[i]=='T':
    increaser=increaser*3
    points+=sc[i]
    i+=1
  points=points*increaser
  maxpoint.append(points)
  return points
 def values(n,string,sc):
  for i in range(n-7):
   maxpoints(n,string[i:],sc)
  return max(maxpoint)
 t=int(input())
 for i in range(t):
  n=int(input())
  string=str(input())
  if n>=8 and n==len(string):
   sc=list(map(int,input().split()))
   print(values(n,string,sc))
   maxpoint=[]
  else:
   print('String is not equals to the length given')
   break
except EOFError:
 pass
