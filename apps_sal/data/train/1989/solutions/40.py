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
            # print(\"{0:b}\".format(key),j)
            if key in presum:

                res = max(res, i - presum[key])

            for x in range(10):
                newKey = key
                if (key >> x) & 1:
                    newKey -= (1 << x)
                    # if key==10:
                    #     print(\"print\",\"{0:b}\".format(newKey),x)
                else:
                    newKey |= (1 << x)
                    # if key==10:
                    #     print(\"print\",\"{0:b}\".format(newKey),x)
                # if 8 in presum:
                #     print(\"res\", presum[8])
                if newKey in presum:

                    res = max(res, i - presum[newKey])
            if key not in presum:
                # print(\"put\",key,i)
                presum[key] = i

        return res
