import sys
f = sys.stdin
out = sys.stdout


def findOperations(s, ind, mid):
    return prefix[mid] - prefix[ind] + abs(s - arr[ind])


(n, s) = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
arr.sort()
mid = n // 2
for i in range(mid):
    if arr[i] > s:
        cnt += abs(s - arr[i])
for i in range(mid + 1, n):
    if arr[i] < s:
        cnt += abs(s - arr[i])
cnt += abs(s - arr[mid])
print(cnt)
