#!/usr/bin/env python3
# -*- coding: utf-8 -*-

(N, K) = list(map(int, input().split()))

ret = 0
for k in range(K):
    nums = list(map(int, input().split()))[1:]

    group = len(nums)
    if nums[0] == 1:
        for j in range(len(nums) - 1):
            if nums[j] + 1 == nums[j + 1]:
                group -= 1
            else:
                break
    ret += group - 1   # split
ret += K + ret - 1   # join
print(ret)
