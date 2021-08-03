class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universal = Counter()
        for b in B:
            universal |= Counter(b)
            # for char, count in Counter(b).items():
            #     universal[char] = max(universal[char], count)

        ans = []
        for a in A:
            c = Counter(a)
            c.subtract(universal)
            if all(v >= 0 for v in c.values()):
                ans.append(a)

        return ans
