import collections


class Solution:

    def findLucky(self, arr):
        l = list((x for (x, y) in collections.Counter(arr).items() if x == y))
        return max(l) if l else -1
