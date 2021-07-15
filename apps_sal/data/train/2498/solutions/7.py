class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        def compare(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if d[w1[i]] < d[w2[i]]:
                    return True
                if d[w1[i]] > d[w2[i]]:
                    return False
            return len(w1) <= len(w2)
        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1]):
                return False
        
        return True
