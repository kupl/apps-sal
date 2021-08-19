class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        lc = [0] * 26
        for b in B:
            for (c, count) in collections.Counter(b).items():
                i = ord(c) - ord('a')
                lc[i] = max(lc[i], count)
        ans = []
        for a in A:
            uni = True
            cter = collections.Counter(a)
            for (c, count) in zip(string.ascii_lowercase, lc):
                if count > cter[c]:
                    uni = False
                    break
            if uni:
                ans.append(a)
        return ans
