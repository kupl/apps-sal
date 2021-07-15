import collections
def solve(arr):
    count = collections.Counter(arr)
    for number in arr:
        if not count[-number]:
            return number
