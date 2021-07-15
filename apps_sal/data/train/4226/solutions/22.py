def remove_smallest(numbers):
    try:
        i = min(range(len(numbers)), key=numbers.__getitem__)
        return numbers[:i] + numbers[i+1:]
    except ValueError:
        return []
