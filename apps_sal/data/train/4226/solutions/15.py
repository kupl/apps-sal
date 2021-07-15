def remove_smallest(numbers):
    i = numbers.index(min(numbers)) if numbers else 0
    return numbers[:i] + numbers[i+1:]
