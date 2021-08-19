class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        maxcb = Counter()
        for b in B:
            for ch in (cb := Counter(b)):
                maxcb[ch] = max(maxcb[ch], cb[ch])
        ans = []
        for a in A:
            ca = Counter(a)
            if all((ca[ch] >= maxcb[ch] for ch in maxcb)):
                ans.append(a)
        return ans
