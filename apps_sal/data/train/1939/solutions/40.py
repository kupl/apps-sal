class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        s = set(wordlist)
        d1 = {}
        d2 = {}
        for word in wordlist:
            if word.lower() not in d1:
                d1[word.lower()] = word
                
        for word in wordlist:
            word1 = word.lower()
            newWords = ['']
            for c in word1:
                newWords2 = []
                for newWord in newWords:
                    if c in 'aeiou':
                        for ch in 'aeiou':
                            newWords2.append(newWord + ch)
                    else:
                        newWords2.append(newWord + c)
                newWords = newWords2
            for newWord in newWords2:
                if newWord not in d2:
                    d2[newWord] = word
                        
        ans = []
        for q in queries:
            ql = q.lower()
            if q in s:
                ans.append(q)
            elif ql in d1:
                ans.append(d1[ql])
            elif ql in d2:
                ans.append(d2[ql])
            else:
                ans.append('')
        return ans
