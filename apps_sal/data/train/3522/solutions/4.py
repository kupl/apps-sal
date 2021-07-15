def max_gap(numbers):
    sorted_n = sorted(numbers)
    return max([sorted_n[i]-sorted_n[i-1] for i in range(1, len(sorted_n))])
