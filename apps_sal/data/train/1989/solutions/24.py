class Solution:
    def longestAwesome(self, s: str) -> int:
        prev = [-1] + [len(s)] * 1024
        best = 1
        mask = 0
        for i in range(len(s)):
            mask ^= 1 << int(s[i])
            # print(i, bin(mask))

            for j in range(10):
                tmp = mask ^ (1 << j)
                if best < i - prev[tmp] + 1:
                    # print('- ' + bin(tmp), i, prev[tmp])
                    best = max(best, i - prev[tmp])
                # best = max(best, i - prev[tmp])

            best = max(best, i - prev[mask])
            prev[mask] = min(prev[mask], i)
        return best
