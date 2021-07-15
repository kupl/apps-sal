def exp_sum(n):
    if n < 0: return 0
    A = [1] + [0]*n
    for i in range(n):
        A = [sum(A[:k+1][::-i-1]) for k in range(n+1)]
    return A[-1]
