class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter = Counter()
        for b in B:
            cb = Counter(b)
            for ch in cb:
                counter[ch] = max(counter[ch], cb[ch])
        ans = []
        for a in A:
            ca = Counter(a)
            if all(ca[ch] >= counter[ch] for ch in counter):
                ans.append(a)
        return ans
