vowels = set([\"a\", \"e\", \"o\", \"i\", \"u\"])

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        first_match = defaultdict(str)
        vowel_match = defaultdict(str)
        word_list = set(wordlist)
        for word in wordlist:
            lower_word = word.lower()
            if not first_match.get(lower_word):
                first_match[lower_word] = word
            letters = list(lower_word)
            self.find_valid_word(letters, 0, word, vowel_match)
                    
            
        results = []
        for word in queries:
            if word in word_list:
                results.append(word)
            else:
                lower_word = word.lower()
                if lower_word in first_match:
                    results.append(first_match[lower_word])
                elif lower_word in vowel_match:
                    results.append(vowel_match[lower_word])
                else:
                    results.append(\"\")
        return results
    
    def find_valid_word(self, letters, start, curr_word, first_match):
        new_str = \"\".join(letters)
        if new_str not in first_match:
            first_match[new_str] = curr_word
        for i in range(start, len(letters)):
            if self.is_vowel(letters[i]):
                for vowel in vowels:
                    letters[i] = vowel
                    valid_word = self.find_valid_word(letters, i + 1, curr_word, first_match)
        return \"\"
          
    def is_vowel(self, char):
        return char in vowels
