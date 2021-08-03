def max_gap(numbers):
    return max(abs(a - b) for a, b in zip(sorted(numbers), sorted(numbers)[1:]))
