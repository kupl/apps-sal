class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        acc = 0
        (tmp, res) = ([], [])
        for w in words:
            if acc + len(w) + len(tmp) > maxWidth:
                for i in range(maxWidth - acc):
                    tmp[i % (len(tmp) - 1 or 1)] += ' '
                res.append(''.join(tmp))
                acc = 0
                tmp = []
            tmp.append(w)
            acc += len(w)
        return res + [' '.join(tmp).ljust(maxWidth)]
