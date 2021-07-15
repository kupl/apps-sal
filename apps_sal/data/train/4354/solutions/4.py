from collections import deque

def padovan(n):
    q = deque([1,1,1], maxlen=3)
    for i in range(n-2):
        q.append(q[0] + q[1])
    return q[-1]
