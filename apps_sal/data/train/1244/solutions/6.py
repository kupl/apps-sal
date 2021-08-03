def add(arr, N, lo, hi, val):
    arr[lo] += val
    if (hi != N - 1):
        arr[hi + 1] -= val


def updateArray(arr, N):
    for i in range(1, N):
        arr[i] += arr[i - 1]


n = 1000000
l = [0] * n
for _ in range(int(input())):
    b, d = map(int, input().split())
    add(l, n, b + 50000, d + 50000, 1)
updateArray(l, n)
print(sum(l) % 1000000007)
