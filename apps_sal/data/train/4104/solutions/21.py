def max_tri_sum(numbers):
    numbers = list(set(numbers))
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    numbers.remove(max2)
    max3 = max(numbers)
    numbers.remove(max3)
    return max1 + max2 + max3
