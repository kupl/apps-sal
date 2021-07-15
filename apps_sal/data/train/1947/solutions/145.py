class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dctB = {}
        for word in B:
            dct = {}
            for ch in word:
                cnt = dct.get(ch)
                dct[ch] = 1 if not cnt else dct[ch] + 1
            for key in dct:
                cnt = dctB.get(key)
                dctB[key] = dct[key] if not cnt else max(cnt, dct[key])

        res = []
        for word in A:
            dct = {}
            univ = True
            for ch in word:
                cnt = dct.get(ch)
                dct[ch] = 1 if not cnt else dct[ch] + 1
            for key in dctB:
                if not dct.get(key) or dct[key] < dctB[key]:
                    univ = False
                    break
            if univ:
                res.append(word)
        return res
