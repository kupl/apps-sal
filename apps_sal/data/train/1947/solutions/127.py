class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        b_union = {}
        for b in B:
            chars = {}
            for c in b:
                chars[c] = chars.get(c, 0) + 1
            for c in chars:
                b_union[c] = max(b_union.get(c, 0), chars[c])

        res = []
        for a in A:
            chars = {}
            for c in a:
                chars[c] = chars.get(c, 0) + 1
            isUniversal = True
            for c in b_union:
                if not c in chars or b_union[c] > chars[c]:
                    isUniversal = False
                    break
            if isUniversal:
                res.append(a)
        return res
