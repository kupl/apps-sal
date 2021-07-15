import heapq
import sys
input=sys.stdin.readline
N,Q=map(int,input().split())

event_list=[]
for i in range(N):
  S,T,X=map(int,input().split())
  event_list.append((S-X-0.5,1,X))
  event_list.append((T-X-0.5,-1,X))
  
dlist=[]
for i in range(Q):
  D=int(input())
  event_list.append((D,0,X))  
  dlist.append(D)
event_list.sort()
#print(event_list)

answer_dic={}
stop_set=set()
hq=[]
for t,f,x in event_list:
  if f==1:
    stop_set.add(x)
    heapq.heappush(hq,x)
  elif f==-1:
    stop_set.remove(x)
  else:
    if len(stop_set)>0:
      while(True):
        if hq[0] in stop_set:
          answer_dic[t]=hq[0]
          break
        else:
          heapq.heappop(hq)
    else:
      answer_dic[t]=-1
#print(answer_dic)

for d in dlist:
  print(answer_dic[d])
