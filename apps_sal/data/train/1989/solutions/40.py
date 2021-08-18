class Solution:
    def longestAwesome(self, s: str) -> int:
        m = collections.defaultdict(lambda: 0)

        def convertToKey():
            x = 0
            for i in range(10):
                x += ((m[i] % 2) << i)
            return x
        presum = {}
        presum[0] = -1
        res = 0
        for i, j in enumerate(s):
            m[int(j)] += 1
            key = convertToKey()
            if key in presum:

                res = max(res, i - presum[key])

            for x in range(10):
                newKey = key
                if (key >> x) & 1:
                    newKey -= (1 << x)
                else:
                    newKey |= (1 << x)
                if newKey in presum:

                    res = max(res, i - presum[newKey])
            if key not in presum:
                presum[key] = i

        return res
