class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        res = [[0]]
        result = []
        for word in words:
            if len(word) + res[-1][-1] + (len(res[-1]) - 1) <= maxWidth:
                res[-1].insert(-1, word)
                res[-1][-1] += len(word)
            else:
                res.append([word, len(word)])

        for index, i in enumerate(res):
            if index != len(res) - 1 and (len(i) - 2) != 0:
                for j in range((maxWidth - i[-1]) % (len(i) - 2)):
                    i[j] = i[j] + " "

        for index, i in enumerate(res):
            if index != len(res) - 1 and (len(i) - 2) != 0:
                result.append((" " * ((maxWidth - i[-1]) // (len(i) - 2))).join(i[:-1]))
            else:
                result.append(" ".join(i[:-1]) + " " * (maxWidth - i[-1] - (len(i) - 2)))
        return result
