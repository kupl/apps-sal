class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=collections.Counter(chars)
        res=0
        
        def valid(word):
            s=collections.Counter(word)
            for ch in s:
                if ch not in c or s[ch]>c[ch]:
                    return False
            return True
        
        for word in words:
            if valid(word):
                res+=len(word)
        return res

