def lower(y):return y.lower()
class Solution:
    
    def checkvowel(self,word,dic,vowels,Results):
        vowelWord = ''
        for y in word:
            if y in vowels:vowelWord+='_'
            else :vowelWord+=lower(y)
        if vowelWord in dic:
            Results += [dic[vowelWord]]
            return True
        else :return False
            
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        dic_vowels = {}
        for x in wordlist: 
            vowelWord = ''
            for y in x:
                if lower(y) in vowels:vowelWord+='_'
                else :vowelWord+=lower(y)
            if vowelWord not in dic_vowels:
                dic_vowels[vowelWord] = x
        
        wordlist_ = {}
        for x in wordlist:
            if lower(x) not in wordlist_:
                wordlist_[lower(x)]=x
        
        Results = []
        for word in queries:
            if word in wordlist:
                Results += [word]
            elif lower(word) in wordlist_:
                Results += [wordlist_[lower(word)]]
            elif self.checkvowel(lower(word),dic_vowels,vowels,Results):
                pass
            else :Results+=[\"\"]
        return Results
    
            
