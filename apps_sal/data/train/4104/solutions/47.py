def max_tri_sum(numbers):
    numbers.sort(reverse=True)
    max_numbers = list(dict.fromkeys(numbers))
    max_sum = sum(max_numbers[:3])
    return max_sum
