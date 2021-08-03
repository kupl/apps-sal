from collections import defaultdict

class Solution:
    def getBitRepr(word):
        \"\"\"
        >>> Solution.getBitRepr('abc')
        7
        \"\"\"
        result = 0
        for char in word:
            result |= (1 << (ord(char) - ord('a')))
        return result

    def countCanonicalWords(words):
        \"\"\"
        >>> Solution.countCanonicalWords(['abc', 'bca'])
        {7: 2}
        \"\"\"
        countMap = defaultdict(int)
        for word in words:
            bitMask = Solution.getBitRepr(word)
            countMap[bitMask] += 1
        return countMap

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        canonicalWordCount = Solution.countCanonicalWords(words)
        puzzlesMasks = [Solution.getBitRepr(x) for x in puzzles]
        result = []

        for i, puzzleBitMask in enumerate(puzzlesMasks):
            matchCount = 0
            candidateWordMask = puzzleBitMask
            firstCharMask = Solution.getBitRepr(puzzles[i][0])
            while candidateWordMask != 0:
                if (candidateWordMask & firstCharMask != 0):
                   matchCount += canonicalWordCount[candidateWordMask]
                candidateWordMask = (candidateWordMask - 1) & puzzleBitMask
            result.append(matchCount)
        return result
