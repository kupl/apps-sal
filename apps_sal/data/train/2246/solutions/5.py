import sys
from queue import PriorityQueue
(n, k) = list(map(int, input().split()))
t = list(map(int, input().split()))
a = int(input())
c = list(map(int, input().split()))
f = 1
cost = 0
m_q = PriorityQueue()
for i in range(n):
    if k + a * (i + 1) < t[i]:
        print(-1)
        break
else:
    for j in range(n):
        if k < t[j]:
            m_q.put(c[j])
            while m_q.qsize() > 0:
                cost += m_q.get()
                k = k + a
                if k >= t[j]:
                    break
        else:
            m_q.put(c[j])
    print(cost)
