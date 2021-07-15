from queue import PriorityQueue 
N, K = tuple(map(int, input().split()))
X = list(map(int, input().split()))
A = int(input())
C = list(map(int, input().split()))
m_q = PriorityQueue()
m = 0
for i in range(N):
    if K < X[i]:
        m_q.put(C[i])
        while m_q.qsize() > 0:
            K += A
            m += m_q.get()
            if K >= X[i]:
                break
        if K < X[i]:
            m=-1
            break    
    else:
        m_q.put(C[i])
print(m)

