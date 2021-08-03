def max_gap(numbers):
    A = sorted(numbers)
    return max([abs(A[i] - A[i + 1]) for i in range(len(A) - 1)])
