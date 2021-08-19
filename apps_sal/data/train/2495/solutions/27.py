from collections import Counter


class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = Counter(target)
        c2 = Counter(arr)
        return not set(c1.keys()).symmetric_difference(set(c2.keys())) and all([c1[k1] == c2[k1] for k1 in c1])
