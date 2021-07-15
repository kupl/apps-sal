def find_missing_number(numbers):
    if numbers == []:return 1
    diff = list(set(range(1, len(numbers)+1))- set(numbers))
    if diff == []:return max(numbers)+1
    return diff[0]
