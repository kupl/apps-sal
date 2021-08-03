class Solution:
    def maskVowels(self, word) -> str:
        return \"\".join('*' if c in 'aeiou' else c
                           for c in word)
        # VOWELS = ['a', 'e', 'i', 'o', 'u']
        # masked_word = word
        # for vowel in VOWELS:
        #     masked_word = masked_word.replace(vowel, '_')
        # return masked_word
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        map = {}
        output = []
                       
        for word in reversed(wordlist):
            lower = word.lower()
            map[lower] = word
            masked_word = self.maskVowels(lower)
            map[masked_word] = word
        
        
        for word in queries:
            word_lower = word.lower()
            word_masked = self.maskVowels(word_lower)
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
   
