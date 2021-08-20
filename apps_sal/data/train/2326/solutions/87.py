from collections import defaultdict


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    min_inds = defaultdict(lambda: 10 ** 5)
    nums = defaultdict(lambda: 0)
    for (ind, a) in enumerate(A):
        min_inds[a] = min(min_inds[a], ind)
        nums[a] += 1
    min_inds = sorted(list(map(list, min_inds.items())), key=lambda x: x[0])
    min_inds.append([10 ** 9 + 1, 10 ** 5])
    nums = sorted(list(map(list, nums.items())), key=lambda x: x[0])
    nums.append([0, 0])
    for i in range(len(min_inds) - 2, -1, -1):
        min_inds[i][1] = min(min_inds[i][1], min_inds[i + 1][1])
        nums[i][1] += nums[i + 1][1]
        ans[min_inds[i][1]] += nums[i][1] * (nums[i][0] - nums[i - 1][0])
    return ans


print(*solve(), sep='\n')
