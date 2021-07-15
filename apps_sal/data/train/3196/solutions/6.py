from bisect import bisect_left, bisect_right
memo = [0, 1]

def triangular_range(start, stop):
    while memo[-1] <= stop: memo.append(memo[-1] + len(memo))
    return {i:memo[i] for i in range(bisect_left(memo, start), bisect_right(memo, stop))}
