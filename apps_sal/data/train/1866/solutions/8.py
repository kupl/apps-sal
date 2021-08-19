class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0:
            return [' '.join(words)]
        words = words[:]
        results = []
        while words:
            run = []
            c = 0
            while words:
                pad = 1 if run else 0
                if len(words[0]) + pad + c > maxWidth:
                    spaces = maxWidth - sum([len(w) for w in run])
                    if len(run) == 1:
                        line = ''.join(run + [' '] * spaces)
                        assert len(line) == maxWidth
                        results.append(line)
                    else:
                        eachSpace = spaces // (len(run) - 1)
                        extraSpaces = spaces % (len(run) - 1)
                        line = []
                        for i in range(len(run)):
                            line.append(run[i])
                            if i != len(run) - 1:
                                line.append(' ' * eachSpace)
                                if extraSpaces > 0:
                                    line.append(' ')
                                    extraSpaces -= 1
                        line = ''.join(line)
                        assert len(line) == maxWidth, len(line)
                        results.append(line)
                    break
                else:
                    if run:
                        c += 1
                    w = words.pop(0)
                    run.append(w)
                    c += len(w)
        if run:
            line = ' '.join(run)
            line += ' ' * (maxWidth - len(line))
            results.append(line)
        return results
