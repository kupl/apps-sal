# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = map(int,readline().split())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,readline().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    

order = []
parent = [-1]*n
st = [0]
while st:
    v = st.pop()
    order.append(v)
    for c in g[v]:
        if parent[v] != c:
            parent[c] = v
            st.append(c)

INF = 1<<30
high = [INF]*n
low = [-INF]*n
val = [INF]*n

k, = map(int,readline().split())
for _ in range(k):
    v,p = map(int,readline().split())
    high[v-1] = low[v-1] = val[v-1] = p

for v in order[:0:-1]:
    p = parent[v]
    #elif val[v]== INF: # vに好きな数書ける
    h,l = high[v]+1,low[v]-1
    
    if h >= INF:
        pass
    elif high[p]>=INF:
        high[p] = h
        low[p] = l
    elif (high[p]-h)&1==0: #偶奇一致
        if h < high[p]: high[p] = h
        if l > low[p]: low[p] = l
        if high[p] < low[p]:
            print("No")
            break
    else: #偶奇違ってダメ
        print("No")
        break
    #print(v,val,high,low)
    
else: #OK
    print("Yes")
    for v in order:
        if val[v] == INF:
            val[v] = low[v]
        for c in g[v]:
            high[c] = min(high[c],val[v]+1)
            low[c] = max(low[c],val[v]-1)
    
    
    print(*val,sep="\n")







