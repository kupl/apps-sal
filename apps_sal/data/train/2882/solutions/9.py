def cumulative_triangle(n):
    N = n * (n+1) // 2
    prev = n * (n-1) // 2
    return N * (N+1) // 2 - prev * (prev+1) // 2
