class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        res = []
        currFill = 0
        start = -1
        for i in range(len(words) + 1):
            if i < len(words) and len(words[i]) + currFill <= maxWidth:
                if currFill == 0:
                    start = i
                currFill += len(words[i]) + 1
            else:
                currFill -= 1
                extra = maxWidth - currFill
                numwords = i - start
                spaces = [1 for _ in range(numwords)]
                if numwords == 1 or i == len(words):
                    spaces[-1] = extra
                else:
                    spaces[-1] = 0
                    for k in range(len(spaces) - 1):
                        spaces[k] += extra // (numwords - 1) + (1 if k < extra % (numwords - 1) else 0)
                curr = ''
                for k in range(len(spaces)):
                    curr += words[k + start] + ' ' * spaces[k]
                res.append(curr)
                currFill = len(words[i]) + 1 if i < len(words) else 0
                start = i
        return res
