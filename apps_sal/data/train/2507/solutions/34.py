import copy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = dict()
        for c in chars:
            if c not in s:
                s[c] = 0
            
            s[c] += 1
    
        t = 0
        for word in words:
            s_copy = copy.deepcopy(s)
            valid = True
            for letter in word:
                if letter not in s_copy:
                    valid = False
                    break
                else:
                    s_copy[letter] -= 1
                    if s_copy[letter] == 0:
                        del s_copy[letter]
            if valid:
                t += len(word)
            
        return t

