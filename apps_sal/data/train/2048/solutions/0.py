import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
total = sum(nums)
avg = int(total / n)

def check1(nums, target, K):
    for x in nums:
        if K < 0:
            return False
        if x < target:
            K -= target - x
    return K >= 0

def check2(nums, target, K):
    for x in nums:
        if K < 0:
            return False
        if x > target:
            K -= x - target
    return K >= 0

l1, r1 = min(nums), avg + 1
while l1 + 1 < r1:
    mid = (l1 + r1) >> 1
    if check1(nums, mid, k):
        l1 = mid
    else:
        r1 = mid

if check2(nums, avg + (0 if total % n == 0 else 1), k):
    r2 = avg + (0 if total % n == 0 else 1)
else:
    l2, r2 = avg + (0 if total % n == 0 else 1), max(nums)
    while l2 + 1 < r2:
        mid = (l2 + r2) >> 1
        if check2(nums, mid, k):
            r2 = mid
        else:
            l2 = mid

print(r2 - l1)
