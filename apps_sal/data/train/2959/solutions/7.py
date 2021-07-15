def optimal_number_of_coins(n, a):
    q = [float('inf')] * (n+1)
    q[0] = 0
    for i in range(1, n+1):
        q[i] = min(q[i-x]+1 for x in a if x <= i)
    return q[n]
