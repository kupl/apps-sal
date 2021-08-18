def super_sum(D, N):
    count = 0
    result = 0
    while ((N - 1) - count) >= 1:
        result += ((N - 1) - count) * (N ** (D - 1))
        count += 1
    return result * D
