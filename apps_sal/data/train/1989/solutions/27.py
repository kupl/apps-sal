class Solution:
    def longestAwesome(self, s: str) -> int:

        def getMatchingMasks(mask):
            st = set([mask])

            for i in range(10):
                st.add(mask ^ (1 << i))

            return st

        mask = 0

        maskDict = dict()

        maskDict[0] = -1

        ans = 0
        for idx, ch in enumerate(s):
            digitVal = int(ch)

            mask ^= (1 << digitVal)

            for match in getMatchingMasks(mask):
                if match in maskDict:
                    ans = max(ans, idx - maskDict[match])

            if mask not in maskDict:
                maskDict[mask] = idx

        return ans
