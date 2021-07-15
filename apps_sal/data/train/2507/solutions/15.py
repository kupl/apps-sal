class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        # go through each word:
        goodCount = 0
        for word in words:
            # go through each letter in each word:
            wordLen = len(word)
            letterCount = 0
            chars_list = list(chars)
            for letter in word:
                if letter in chars_list:
                    letterCount += 1
                    chars_list.remove(letter)
            if letterCount == wordLen:
                goodCount +=letterCount
        return goodCount

