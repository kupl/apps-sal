class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if not wordlist or not queries:
            return None
        
        wordlistSet = set(wordlist)
        wordUpper ={}
        wordVowels = {}
        res = []
        
        
        def getwordWithVowelErrors(s):
            newWord =\"\"
            vowels = {'a','e','i','o','u'}
            for ch in s:
                if ch in vowels:
                    newWord += \"*\"
                else:
                    newWord += ch
            return newWord
                    
        
        
        for  w in wordlist:
            lower = w.lower()
            if lower not in wordUpper:
                wordUpper[lower] = w
                
            wordWithVowelErrors = getwordWithVowelErrors(lower)
            if wordWithVowelErrors not in wordVowels:
                wordVowels[wordWithVowelErrors] = w
                
        for q in queries:
            if q:
                lower = q.lower()
                wordWithVowelErrors = getwordWithVowelErrors(lower)
                if q in wordlistSet:
                    res.append(q)
                elif lower in wordUpper:
                    res.append(wordUpper[lower])
                elif wordWithVowelErrors in wordVowels:
                    res.append(wordVowels[wordWithVowelErrors])
                else:
                    res.append(\"\")
                    
        return res
        
