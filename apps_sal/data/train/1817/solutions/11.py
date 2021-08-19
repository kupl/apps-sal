class Solution:

    def reorganizeString(self, S):
        c = collections.Counter(S)
        if max(c.values()) <= (len(S) + 1) / 2:
            res = ''
            while c:
                out = c.most_common(2)
                if len(out):
                    res += out[0][0]
                    c[out[0][0]] -= 1
                if len(out) > 1:
                    res += out[1][0]
                    c[out[1][0]] -= 1
                c += collections.Counter()
            return res
        return ''
        '\n         :type S: str\n         :rtype: str\n         '
