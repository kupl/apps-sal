def remove_smallest(numbers):
    n = numbers[:]
    n and n.remove(min(n))
    return n
