class Solution:
    def reorderSpaces(self, text: str) -> str:

        words = text.split(' ')
        words = list(filter(lambda x: len(x) > 0, words))

        wordsLen = len(words)
        spacesLen = text.count(' ')

        if(wordsLen == 1):
            return words[0] + ' ' * spacesLen
        evenDistSpaces = spacesLen // (wordsLen - 1)
        endDistSpaces = spacesLen % (wordsLen - 1)

        space = ' ' * evenDistSpaces
        end = ' ' * endDistSpaces

        print(len(space), len(end))

        resultString = space.join(words)
        resultString += end

        return resultString
