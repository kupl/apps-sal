def solve(arr):
    return sum(num + i in arr and num + 2 * i in arr for i in range(1, arr[-2] + 1)\
        for num in arr[:-2])

