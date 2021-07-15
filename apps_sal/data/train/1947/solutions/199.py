class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        need = Counter()
        
        for word in B:
            word_count = Counter(word)
            for k, v in list(word_count.items()):
                need[k] = max(need[k], v)

        def is_subset(word):
            word_count = Counter(word)

            for c in need:
                word_count[c] -= need[c]
                if word_count[c] < 0:
                    return False
            
            return True
            
        res = []
        for word in A:
            if is_subset(word):
                res.append(word)
        
        return res


