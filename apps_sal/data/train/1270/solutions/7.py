tc = int(input())
while tc!= 0:
 count=0
 n,k= map(int, input().split())
 h = sorted(map(int,input().split()))
 h.reverse()
 queue = [h[0]]
 sum2 = h[0]
 res = -1
 for i in range(1,len(h)):
  queue2=[]
  s=set()
  sum2+= h[i]
  for x in queue:
   if x not in s:
    queue2.append(x)
    s.add(x)
   if h[i] not in s:
    queue2.append(h[i])
    s.add(h[i])
   if x+h[i] not in s:
    queue2.append(x+h[i])
    s.add(x+h[i])
   if(x+h[i])>=k and (sum2-x-h[i])>=k:
    res= i+1
    break
   if (h[i]>=k) and (sum2-h[i])>=k:
    res= i+1
    break
  if res!= -1:
   break
  queue = queue2
 print(res)
 tc-= 1
