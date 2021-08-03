from collections import Counter


def solve(arr):
    result = []
    dic = Counter(arr)
    for value in arr:
        if dic[value] == 1:
            result.append(value)
        else:
            dic[value] -= 1
    return result
