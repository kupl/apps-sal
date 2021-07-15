from itertools import groupby

def sum_of_regular_numbers(arr):
    res = [[b-a, i] for i, a, b in zip(range(len(arr)), arr, arr[1:])]
    ans = 0
    for _, g in groupby(res, key=lambda x: x[0]):
        lst = list(g)
        if len(lst) > 1:
            ans += sum(arr[lst[0][1]:lst[-1][1]+2])
    return ans
