import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B_count = collections.Counter()
        for ele in B:
            B_count |= collections.Counter(ele)
        res = []
        for ele in A:
            ele_count = collections.Counter(ele)
            for letter, count in list(B_count.items()):
                if ele_count[letter] < count:
                    break
            else:
                res.append(ele)
        return res
