class Solution:    
    def __init__(self):
        self.words = set()
        self.dict_cap = {}
        self.dict_vowel = {}
        
    def _populate_dicts(self, wordlist):
        for word in wordlist:
            self.words.add(word)
            self.dict_cap[word.lower()] = self.dict_cap.setdefault(word.lower(), word)
            self.dict_vowel[self._jokerize_vowels(word.lower())] = self.dict_vowel.setdefault(self._jokerize_vowels(word.lower()), word)
        print(self.dict_vowel)
    
    def _jokerize_vowels(self, word):
        return \"\".join(\"*\" if l.lower() in \"aeiou\" else l for l in word)
    
    def check_word(self, word):
        if word in self.words:
                return word
            
        elif (word := word.lower()) in self.dict_cap:
            return self.dict_cap[word]

        elif (word := self._jokerize_vowels(word)) in self.dict_vowel:
            return self.dict_vowel[word]

        else:
            return \"\"
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        self._populate_dicts(wordlist)

        return [self.check_word(q) for q in queries]
