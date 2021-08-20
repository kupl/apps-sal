class Solution:

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        capLookup = {}
        vowelLookup = {}
        res = []
        for word in wordlist:
            if word.lower() not in capLookup:
                capLookup[word.lower()] = word
            starword = ''.join(('*' if l in 'aeiou' else l for l in word.lower()))
            if starword not in vowelLookup:
                vowelLookup[starword] = word
        for query in queries:
            if query in wordlist:
                res.append(query)
                continue
            if query.lower() in capLookup:
                res.append(capLookup[query.lower()])
                continue
            starquery = ''.join(('*' if l in 'aeiou' else l for l in query.lower()))
            if starquery in vowelLookup:
                res.append(vowelLookup[starquery])
                continue
            else:
                res.append('')
        return res
