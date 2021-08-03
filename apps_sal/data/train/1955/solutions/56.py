import collections
import functools
import heapq
import itertools
import sys
from functools import lru_cache
from typing import List
from fractions import gcd

'''
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

注意这不是一道dfs或bfs题。

如果两个位置可以任意交换，则两个位置排序即可。

如果(1,2), (2,3), 则1 2 3位置排序即可。

所以问题是找到并查集, 然后直接排序即可。
'''


class UFSet:
    def __init__(self, n):
        self.dp = [-1 for _ in range(n)]

    def find(self, x):
        if self.dp[x] < 0:
            return x
        self.dp[x] = self.find(self.dp[x])
        return self.dp[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        self.dp[root_x] += self.dp[root_y]
        self.dp[root_y] = root_x

    def get_group(self):
        ret = collections.defaultdict(list)
        for i in range(len(self.dp)):
            ret[self.find(i)].append(i)
        return ret


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        ufs = UFSet(n)
        for i, j in pairs:
            ufs.union(i, j)
        group_map = ufs.get_group()
        ret = [i for i in s]
        for group in list(group_map.values()):
            sort_group = sorted([s[i] for i in group])
            for i, j in zip(group, sort_group):
                ret[i] = j
        return ''.join(ret)
