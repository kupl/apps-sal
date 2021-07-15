class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def canonicalize(word: str) -> str:
            chars = list(word.lower())
            for i in range(len(chars)):
                if chars[i] in ['a', 'e', 'i', 'o', 'u']:
                    chars[i] = '.'

            return ''.join(chars)

        def remove_vowel(word: str) -> str:
            chars = list(word)
            for i in range(len(chars)):
                if chars[i] in ['a', 'e', 'i', 'o', 'u']:
                    chars[i] = '.'
                    
            return ''.join(chars)
            
        lowercase_wordlist = {}
        for i in range(len(wordlist)-1, -1, -1):
            word = wordlist[i]
            lowercase_wordlist[word.lower()] = i
            
        antivowel = {}
        for i in range(len(wordlist)-1, -1, -1):
            word = remove_vowel(wordlist[i].lower())
            antivowel[word] = i
        
        # canonical_wordlist = [canonicalize(word) for word in wordlist]
        # print(canonical_wordlist)
        wordlist_lookup = {}
        for i in range(len(wordlist)-1, -1, -1):
            wordlist_lookup[wordlist[i]] = i

        def solve(query):
            #canonical_query = canonicalize(query)
            if query in wordlist_lookup:
                return query
            elif query.lower() in lowercase_wordlist:
                return wordlist[lowercase_wordlist[query.lower()]]
            elif remove_vowel(query.lower()) in antivowel:
                return wordlist[antivowel[remove_vowel(query.lower())]]
            else:
                return \"\"
        
        return [solve(query) for query in queries]

