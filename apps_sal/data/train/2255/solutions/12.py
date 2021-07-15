from collections import Counter

def check_funny(n, nums):
    cnt = {0: Counter(), 1: Counter()}
    cnt[1][0] = 1
    x = 0
    res = 0
    for i in range(n):
        x ^= nums[i]
        res += cnt[i % 2][x]
        cnt[i % 2][x] += 1
    return res


n = int(input())
nums = list(map(int, input().split()))
print(check_funny(n, nums))

