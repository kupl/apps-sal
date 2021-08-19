class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_representation = [0] * 26

        def str2list(s):
            li = [0] * 26
            for c in s:
                li[ord(c) - ord('a')] += 1
            return li

        def is_greater(li1, li2):
            for i in range(26):
                if li1[i] < li2[i]:
                    return False
            return True
        for s in B:
            b_representation = [max(tmp1, tmp2) for (tmp1, tmp2) in zip(b_representation, str2list(s))]
        res = []
        for s in A:
            if is_greater(str2list(s), b_representation):
                res.append(s)
        return res
