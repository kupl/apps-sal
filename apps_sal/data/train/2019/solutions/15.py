from math import ceil
n = int(input())
arr = list(map(int, input().split()))
print(max(max(arr), ceil(sum(arr) / (n - 1))))
