from collections import deque

def count_ways(n, k):
    rs = deque(maxlen=k)
    rs.append(1)
    for _ in range(n):
        rs.append(sum(rs))
    return rs[-1]
