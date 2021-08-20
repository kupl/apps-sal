import math


def find(n):
    first = [0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21]
    if n < 13:
        return first[n]
    seq = [1, 1, 3, 5]
    k = 3
    add = 3
    count = 2
    sum = 11
    while True:
        if sum + add * len(seq) >= n:
            return math.ceil((n - sum) / len(seq)) + seq[len(seq) - 1]
        seq.append(seq[len(seq) - 1] + add)
        sum += add * (len(seq) - 1)
        count -= 1
        if count == 0:
            k += 1
            add += 1
            count = seq[k] - seq[k - 1]
