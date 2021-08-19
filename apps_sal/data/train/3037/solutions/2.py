from collections import Counter


def obtain_max_number(arr):
    count = Counter(arr)
    while any((value > 1 for value in list(count.values()))):
        n = next((key for key in count if count[key] > 1))
        count[n] -= 2
        count[n * 2] += 1
    return max(count)
