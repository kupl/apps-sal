class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        all_words = set(wordlist)
        lowered = {}
        transformed = {}
        
        VOWELS = 'aeiou'
        
        def transform(word):
            return ''.join(['_' if char in VOWELS else char for char in word])
        
        for word in wordlist:
            lowered.setdefault(word.lower(), word)
            transformed.setdefault(transform(word.lower()), word)
        
        res = []
        for word in queries:
            if word in all_words:
                res.append(word)
                continue
            
            low = word.lower()
            if low in lowered:
                res.append(lowered[low])
                continue
            
            tran = transform(low)
            if tran in transformed:
                res.append(transformed[tran])
            else:
                res.append(\"\")
        
        return res
