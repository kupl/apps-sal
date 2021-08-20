class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        if len(chars) == 0 or len(words) == 0:
            return 0
        letterCounts = {}
        for c in chars:
            if str(c) in letterCounts:
                letterCounts[str(c)] += 1
            else:
                letterCounts[str(c)] = 1
        totalLength = 0
        for word in words:
            currentLetterCounts = {}
            for letter in word:
                if str(letter) in currentLetterCounts:
                    currentLetterCounts[str(letter)] += 1
                else:
                    currentLetterCounts[str(letter)] = 1
            valid = True
            for (key, value) in currentLetterCounts.items():
                if key not in letterCounts:
                    valid = False
                    break
                if letterCounts[key] < value:
                    valid = False
                    break
            if valid:
                totalLength += len(word)
        return totalLength
