class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_sum = 0
        
        def isValid(word, chars):
            for letter in word:
                if chars[letter] > 0:
                    chars[letter] -= 1
                else:
                    return False
            return True
        
        for word in words:
            counter = Counter(chars)
            if isValid(word, counter):
                char_sum += len(word)
        
        return char_sum
        
        
    

