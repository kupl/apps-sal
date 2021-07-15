from collections import Counter 

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        s = Counter()
        for b in B: 
            s = s | Counter(b)
            
        words = []
        def is_universal(word: str):
            word_counts = Counter(word)
            if len(word) < len(s): 
                return False
            for k, v in list(s.items()): 
                if k not in word_counts: 
                    return False 
                if word_counts[k] < v: 
                    return False 
            return True
        
        for word in A: 
            if is_universal(word): 
                words.append(word)
        
        return words
            

