class Solution:
    def replaceVowels(self, s):
        return \"\".join(['*' if x in ['a','e','i','o','u'] else x for x in s.lower()])
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = [\"\" for q in queries]
        
        capitalizationDict = {}
        vowelDict = {}
        
        for w in wordlist:
            w_lower = w.lower()
            if w_lower not in capitalizationDict:
                capitalizationDict[w_lower] = []
            capitalizationDict[w_lower].append(w)
            
            w_vowel = self.replaceVowels(w)
            if w_vowel not in vowelDict:
                vowelDict[w_vowel] = []
                
            vowelDict[w_vowel].append(w)
            
        wordSet = set(wordlist)
        
        for i in range(len(queries)):
            if queries[i] in wordSet:
                result[i] = queries[i]
            elif queries[i].lower() in capitalizationDict:
                result[i] = capitalizationDict[queries[i].lower()][0]
            elif self.replaceVowels(queries[i]) in vowelDict:
                result[i] = vowelDict[self.replaceVowels(queries[i])][0]
                
        return result
