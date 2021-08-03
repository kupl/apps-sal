from itertools import combinations

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]):
        def code_word(word):
            b = 0
            for c in word:
                b |= 1 << (ord(c) - ord('a'))
            return b
        
        def remove_duplicates(word):
            d = {}
            result = \"\"
            for c in word:
                if c not in d:
                    d[c] = True
                    result += c
            return result
                    
        
        words_bits = defaultdict(int)   
        for word in words:
            b = code_word(word)
            words_bits[b] += 1
            
        for puzzle in puzzles:
            count = 0
            first_letter = 1 << (ord(puzzle[0]) - ord('a'))       
            if not first_letter & code_word(puzzle):
                continue
            p = remove_duplicates(puzzle)
            for i in range(len(p)):
                for c in combinations(p,i + 1):
                    b = code_word(c)
                    if b in words_bits and first_letter & b:
                        count += words_bits[b]
            yield count
        
                
        
