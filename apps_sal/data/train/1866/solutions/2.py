class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        currLine = []
        charCount = 0
        result = []
        for word in words:
            if charCount + len(currLine) + len(word) <= maxWidth:
                charCount += len(word)
                currLine.append(word)
            else:
                thisLine = currLine[0]
                for i in range(1, len(currLine)):
                    thisLine += ' ' * ((maxWidth - charCount) // (len(currLine) - 1))
                    if i <= (maxWidth - charCount) % (len(currLine) - 1):
                        thisLine += ' '
                    thisLine += currLine[i]
                if len(thisLine) < maxWidth:
                    thisLine += ' ' * (maxWidth - len(thisLine))
                result.append(thisLine)
                currLine = [word]
                charCount = len(word)
        if len(currLine) > 0:
            lastLine = ' '.join(currLine)
            if len(lastLine) < maxWidth:
                lastLine += ' ' * (maxWidth - len(lastLine))
            result.append(lastLine)
        if len(result) == 0:
            return ['']
        return result
