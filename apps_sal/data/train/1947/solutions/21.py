from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_hash = {}
        ans = []
        for i in B:
            for j in set(i):
                if j in b_hash:
                    b_hash[j] = max(i.count(j), b_hash[j])
                else:
                    b_hash[j] = i.count(j)

        for wrd in A:
            new_b_hash = b_hash.copy()
            for i in set(wrd):
                if i in b_hash:
                    new_b_hash[i] -= wrd.count(i)
            value_flag = True
            for i in list(new_b_hash.values()):
                if i > 0:
                    value_flag = False
                    break
            if value_flag:
                ans.append(wrd)

        return ans
