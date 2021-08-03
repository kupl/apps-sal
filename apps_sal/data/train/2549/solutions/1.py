class Solution:
    def reorderSpaces(self, text: str) -> str:

        # separate words and spaces
        words = text.split(' ')
        words = list(filter(lambda x: len(x) > 0, words))
        # print(words)

        # get their counts so we can do some math
        wordsLen = len(words)
        spacesLen = text.count(' ')

        # print(wordsLen, spacesLen)
        if(wordsLen == 1):
            return words[0] + ' ' * spacesLen
        evenDistSpaces = spacesLen // (wordsLen - 1)
        endDistSpaces = spacesLen % (wordsLen - 1)

        # print(evenDistSpaces, endDistSpaces)

        space = ' ' * evenDistSpaces
        end = ' ' * endDistSpaces

        print(len(space), len(end))

        resultString = space.join(words)
        resultString += end

        return resultString
