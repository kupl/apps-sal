from collections import defaultdict


def precompute(arr, n, k):
    nonlocal maxdistance
    arr = list(enumerate(arr))
    arr.sort(key=lambda x: -x[1])
    maxdistance[arr[0][0]] = arr[0][1] + k
    for i in range(1, n):
        if arr[i - 1][1] - arr[i][1] <= k:
            maxdistance[arr[i][0]] = maxdistance[arr[i - 1][0]]
        else:
            maxdistance[arr[i][0]] = arr[i][1] + k


def answer(x, y):
    nonlocal maxdistance
    if maxdistance[x - 1] == maxdistance[y - 1]:
        return "Yes"
    return "No"


maxdistance = defaultdict(int)
n, k, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
precompute(arr, n, k)
for _ in range(q):
    x, y = list(map(int, input().split()))
    print(answer(x, y))
