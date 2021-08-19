class Solution:

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        "\n         size = len(S)\n         limit = size//2 + size%2\n         cnt = collections.Counter(S)\n         res = [0]*size\n         i = 0\n         for k, v in cnt.most_common():\n             if v > limit:\n                 return ''\n             for _ in range(v):\n                 if i >= size:\n                     i = res.index(0)\n                 res[i] = k\n                 i += 2\n         return ''.join(res)\n         "
        cnt = collections.Counter(S)
        res = '#'
        while cnt:
            stop = True
            for (k, v) in cnt.most_common():
                if k != res[-1]:
                    stop = False
                    res += k
                    cnt[k] -= 1
                    if not cnt[k]:
                        del cnt[k]
                    break
            if stop == True:
                break
        return res[1:] if len(res) == len(S) + 1 else ''
