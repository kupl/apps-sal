class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def helper(query):
            # check for exact
            if query in wordlist:
                return query
            # check for first case-insensitive match
            if query.lower() in lowercase:
                return wordlist[lowercase[query.lower()]]
                
            # check for vowel error match
            withoutVowelQuery = \"\"
            for char in query:
                if char.lower() in vowels:
                    withoutVowelQuery += '#'
                else:
                    withoutVowelQuery += char.lower()
                    
            if withoutVowelQuery in without_vowel:
                return wordlist[without_vowel[withoutVowelQuery]]
            # else return empty string
            return \"\"
        
        res = []
        
        lowercase = {}
        
        for i, word in enumerate(wordlist):
            if word.lower() not in lowercase:
                lowercase[word.lower()] = i
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        without_vowel = {}
        
        for i, word in enumerate(wordlist):
            newWord = \"\"
            for char in word:
                if char.lower() in vowels:
                    newWord += '#'
                else:
                    newWord += char.lower()
            if newWord not in without_vowel:
                without_vowel[newWord] = i
        
        # print(wordlist)
        # print(lowercase)
        # print(without_vowel)
        
        for query in queries:
            res.append(helper(query))
        return res
