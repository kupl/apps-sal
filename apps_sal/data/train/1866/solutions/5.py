class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        (i, n) = (0, len(words))
        while i < n:
            count = len(words[i])
            last = i + 1
            while last < n and count + len(words[last]) + 1 <= maxWidth:
                count += len(words[last]) + 1
                last += 1
            diff = last - i - 1
            temp = words[i]
            if last == n or diff == 0:
                for j in range(i + 1, last):
                    temp += ' '
                    temp += words[j]
                temp += ' ' * (maxWidth - len(temp))
            else:
                (m, re) = divmod(maxWidth - count, diff)
                for j in range(i + 1, last):
                    temp += ' ' * m
                    if re > 0:
                        temp += ' '
                        re -= 1
                    temp += ' '
                    temp += words[j]
            i = last
            res.append(temp)
        return res
