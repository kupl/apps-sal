class Solution:
    def maskVowels(self, word) -> str:
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        masked_word = word.lower()
        for vowel in VOWELS:
            masked_word = masked_word.replace(vowel, '_')
        return masked_word
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        map = {}
        output = []
                       
        for word in reversed(wordlist):
            # if word.lower() not in map:
            map[word.lower()] = word
            masked_word = self.maskVowels(word)
            map[masked_word] = word
        
        
        for word in queries:
            word_lower = word.lower()
            word_masked = self.maskVowels(word)
            if word in wordlist:
                output.append(word)
            elif word in map:
                output.append(map[word])
            elif word_lower in map:
                output.append(map[word_lower])
            elif word_masked in map:
                output.append(map[word_masked])
            else:
                output.append(\"\")
        
        return output
   
