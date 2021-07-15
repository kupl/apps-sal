from collections import Counter


class Solution:
    def parse_word(self, word):
        return Counter(word)

    def update_counter(self, orig, new):
        for c in new:
            orig[c] = max(new[c], orig[c])
        
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        min_universal = Counter()
        for b in B:
            bc = Counter(b)
            self.update_counter(min_universal, bc)

        universals = []
        for a in A:
            ac = Counter(a)
            is_universal = True
            for c in min_universal:
                if ac[c] < min_universal[c]:
                    is_universal = False
                    break
            if is_universal:
                universals.append(a)
        return universals
            
        

