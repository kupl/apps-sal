from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        b_word = [0] * 26
        
        for word in B:
            for idx, count in enumerate(self.create_char_set(word)):
                b_word[idx] = max(b_word[idx], count)
        
        for word in A:
            a_word = self.create_char_set(word)
            idx = 0
            while idx < len(b_word) and a_word[idx] >= b_word[idx]:
                idx += 1
            if idx == len(b_word):
                res.append(word)
                
        return res
        
        
    
    def create_char_set(self, word):
        char_set = [0] * 26
        for char in word:
            char_set[ord(char) - ord('a')] += 1
        return char_set

