def min_sum(arr):
    cunt = []
    for cum in range(len(arr) // 2):
        cunt.append(min(arr) * max(arr))
        arr.remove(min(arr))
        arr.remove(max(arr))
    return sum(cunt)
