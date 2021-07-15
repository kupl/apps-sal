class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        self.wordset = set(wordlist)
        self.worddict_capitalized = {w.upper() : w for w in wordlist[::-1]}
        self.worddict_vowels = {self.replace_vowels(w.upper()) : w for w in wordlist[::-1]}
        
        #print(self.worddict_vowels)
        
        return [self.correct(q) for q in queries]
    
    def correct(self, q):
        if q in self.wordset:
            return q
        
        if q.upper() in self.worddict_capitalized:
            return self.worddict_capitalized[q.upper()]

        if self.replace_vowels(q.upper()) in self.worddict_vowels:
            return self.worddict_vowels[self.replace_vowels(q.upper())]
        
        return \"\"
    
    def replace_vowels(self, q):
        return q.replace(\"A\", \"!\").replace(\"E\", \"!\").replace(\"I\", \"!\").replace(\"O\", \"!\").replace(\"U\", \"!\")

