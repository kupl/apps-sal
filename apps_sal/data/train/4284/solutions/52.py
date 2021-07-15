def array_leaders(numbers):
    return [n for c,n in enumerate(numbers,1) if n > sum(numbers[c:])]
