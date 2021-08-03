def max_tri_sum(numbers):
    unique = list(set(numbers))
    unique.sort(reverse=True)
    return unique[0] + unique[1] + unique[2]
