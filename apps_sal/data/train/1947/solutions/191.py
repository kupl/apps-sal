import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        if not B:
            return A

        mapB = defaultdict(int)
        for b in B:
            counter = Counter(b)
            for k in counter:
                mapB[k] = max(counter[k], mapB[k])

        res = []
        for a in A:
            countA = Counter(a)
            if all([countA[ch] >= mapB[ch] for ch in mapB]):
                res.append(a)

        return res
