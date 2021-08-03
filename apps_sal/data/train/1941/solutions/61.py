class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def helper(mask, pIdx, i):
            str1 = puzzles[pIdx]
            if i >= len(str1):
                return
            mask2 = mask
            mask2 |= 1 << (ord(str1[i]) - ord('a'))
            if mask2 ^ mask:
                d[mask2].add(pIdx)
                helper(mask2, pIdx, i + 1)
            helper(mask, pIdx, i + 1)

        d = collections.defaultdict(set)
        n = len(puzzles)
        for i, p in enumerate(puzzles):
            mask = 1 << (ord(p[0]) - ord('a'))
            d[mask].add(i)
            helper(mask, i, 1)
        res = [0] * len(puzzles)
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            for idx in d[mask]:
                res[idx] += 1
        return res
