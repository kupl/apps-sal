class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = collections.defaultdict(list)
        capitalization = collections.defaultdict(list)
        
        ans = []
        for word in wordlist:
            w = word.lower()
            for vowel in 'aeiouAEIOU':
                w = w.replace(vowel,\"*\")
            vowels[w].append(word)
        
        for word in wordlist:
            capitalization[word.lower()].append(word)
        wordlist_set = set(wordlist)
        for word in queries:
            if word in wordlist:
                ans.append(word)
                continue
            word_lower = word.lower()
            if word_lower in capitalization:
                ans.append(capitalization[word_lower][0])
                continue
                
            for vowel in 'aeiouAEIOU':
                word_lower = word_lower.replace(vowel,\"*\")
            if word_lower in vowels:
                ans.append( vowels[word_lower][0])
                continue
            else:
                ans.append(\"\")
                
        return ans  
            
