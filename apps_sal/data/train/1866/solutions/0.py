class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def make_str(buffer, length, last):
            if last:
                return ' '.join(buffer) + ' ' * (maxWidth - length)
            space = maxWidth - (length - len(buffer) + 1)
            cnt = len(buffer) - 1
            tmp = ''
            if cnt == 0:
                tmp = buffer[0] + ' ' * space
            else:
                spaces = [space // cnt] * cnt
                for i in range(space % cnt):
                    spaces[i] += 1
                spaces.append(0)
                for s, b in zip(spaces, buffer):
                    tmp += b + ' ' * s
            return tmp

        res = []
        buffer = []
        length = 0
        for w in words:
            lw = len(w)
            if lw > maxWidth:
                continue
            if len(buffer) == 0:
                buffer.append(w)
                length = lw
            elif length + lw + 1 <= maxWidth:
                buffer.append(w)
                length = length + lw + 1
            else:
                tmp = make_str(buffer, length, False)
                res.append(tmp)
                buffer = [w]
                length = lw
        if len(buffer) > 0:
            tmp = make_str(buffer, length, True)
            res.append(tmp)

        return res
