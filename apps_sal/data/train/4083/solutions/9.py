from collections import Counter


def performant_smallest(arr, n):
    counts = Counter(arr)
    total = 0
    num_max = 0
    result = []
    for item, count in sorted(counts.items()):
        if total + count >= n:
            maximum = item
            max_max = n - total
            break
        total += count
    for element in arr:
        if element < maximum:
            result.append(element)
        elif element == maximum and num_max < max_max:
            result.append(element)
            num_max += 1
    return result
