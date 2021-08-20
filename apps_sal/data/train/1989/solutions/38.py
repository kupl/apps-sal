class Solution:

    def longestAwesome(self, s: str) -> int:
        subsum = [0]
        rtn = 0
        first_appear = {}
        first_appear[0] = 0
        for (i, x) in enumerate(s):
            subsum.append(subsum[i] ^ 1 << int(x))
            if subsum[i + 1] not in first_appear:
                first_appear[subsum[i + 1]] = i + 1
            else:
                rtn = max(rtn, i + 1 - first_appear[subsum[i + 1]])
            for j in range(10):
                if subsum[i + 1] ^ 1 << j in first_appear:
                    rtn = max(rtn, i + 1 - first_appear[subsum[i + 1] ^ 1 << j])
        return rtn
