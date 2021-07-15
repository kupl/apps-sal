def super_sum(D, N):
    return (N ** D) * (D) * ((N - 1) // 2) if N % 2 else ((N ** D) // 2) * (D) * (N - 1)
