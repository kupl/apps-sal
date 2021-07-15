import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        n = 0
        for word in words:
            count = 0
            for letter in word:
                if letter in chars and word.count(letter) <= chars.count(letter):
                    count += 1
            if count == len(word):
                n += len(word)
        return n 
                    

