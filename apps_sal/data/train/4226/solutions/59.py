def remove_smallest(numbers):
    if numbers:
        idx_map = {}
        for i, number in enumerate(numbers):
            if number not in list(idx_map.keys()):
                idx_map[number] = i
        smallest = min(numbers)
        result = numbers.copy()
        result.pop(idx_map[smallest])
        return result
    else:
        return numbers
