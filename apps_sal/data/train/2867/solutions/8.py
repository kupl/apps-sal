from collections import Counter


def fix_progression(arr):
    lst = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) % (j - i) == 0:
                dif = (arr[j] - arr[i]) // (j - i)
                s = arr[i] - i * dif
                lst.append((s, dif))
    c = Counter(lst).most_common()[0]
    count = 0
    for i in range(len(arr)):
        if arr[i] != c[0][0] + i * c[0][1]:
            count += 1
    return count
