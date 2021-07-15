t = int(input())
for z in range(t):
 first = list(map(int,input().split()))
 second = list(map(int,input().split()))
 length = len(set(second))
 req = 0
 sumi = 0
 for i in range(first[1]):
  req = req+second[i]
 if(length==len(set(second[0:first[1]]))):
  sumi = req
 cp = 0
 for i in range(first[1]+1, first[0]+1):
  req = req - second[cp]+second[i-1]
  if(length == len(set(second[cp+1:i]))):
   if(sumi<req):
    sumi=req
  cp = cp+1
 print(sumi)

