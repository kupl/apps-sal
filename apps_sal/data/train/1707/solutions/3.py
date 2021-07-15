def cut_log(p, n):
    q = [0]
    for j in range(1, n+1):
        q.append(max(p[i] + q[j-i] for i in range(1, j+1)))
    return q[n]
