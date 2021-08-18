class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        goodCount = 0
        for word in words:
            wordLen = len(word)
            letterCount = 0
            chars_list = list(chars)
            for letter in word:
                if letter in chars_list:
                    letterCount += 1
                    chars_list.remove(letter)
            if letterCount == wordLen:
                goodCount += letterCount
        return goodCount
