N,T = list(map(int, input().split()))
A = list(map(int, input().split()))

back = [(0,0)]*(N+1)
# (a,b): b is # of a
def heapsort(lst):
    h = []
    for value in lst:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]

for i in range(N, 0, -1):
    if A[i-1] > back[i][0]:
        back[i-1] = (A[i-1], 1)
    elif A[i-1] == back[i][0]:
        back[i-1] = (A[i-1], back[i][1] + 1)
    else:
        back[i-1] = back[i]

anslst = []
from heapq import heappush, heappop

for i in range(N):
    heappush(anslst, (- (back[i][0] - A[i]), back[i][1]) )
anslst = heapsort(anslst)


val = - anslst[0][0]

ans = 0
for i in range(N):
    if val != - anslst[i][0]:
        break
    ans += anslst[i][1] 
print(ans)


