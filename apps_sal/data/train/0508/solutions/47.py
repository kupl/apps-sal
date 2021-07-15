from heapq import heappop,heappush

N,Q=map(int,input().split())


event=[]
q=[]
for _ in range(N):
    S,T,X=map(int,input().split())
    event.append([S-X,1,X])
    event.append([T-X,-1,X])

for i in range(Q):
    event.append([int(input()),2,i])

stop_set=set()
event.sort()
q=[]

for pos,m,x in event:
    if m==-1:
        stop_set.remove(x)
        
    elif m==1:
        #heappushする時点でqはソートされている
        heappush(q,x)
        stop_set.add(x)
    
    else:
        #この時点でのstop_setは、i番目の人が遭遇する通行止めの座標
        #この時点でのqは今までstopになった座標
        while q:
            #qはソート済なので、q[0]は最小値　それがstop_setから外れている場合、heappopでそれを排除する
            if q[0] not in stop_set:
                heappop(q)
            #q[0]がstop_setから外れてない場合、それ以降のqも外れていないのでbreak    
            else:
                break

        if q:
            print(q[0])
        else:
            print(-1)
