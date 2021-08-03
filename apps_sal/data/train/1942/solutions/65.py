class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        idx = {}
        encoded = []
        n = len(favoriteCompanies)
        for l in favoriteCompanies:
            b = 0
            for c in l:
                idx.setdefault(c, len(idx))
                b |= 1 << idx[c]
            encoded.append(b)
        ans = []
        for i, b1 in enumerate(encoded):
            for b2 in encoded:
                if b1 | b2 == b2 and b1 != b2:
                    break
            else:
                ans.append(i)
        return ans
