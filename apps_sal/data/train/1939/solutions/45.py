from collections import defaultdict

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        VOWELS = {\"a\", \"e\", \"i\", \"o\", \"u\"}
        
        wordDict = {}
        for i in range(0, len(wordlist)):
            wordDict[wordlist[i]] = i
            
        wordIDict = defaultdict(list)
        for i in range(0, len(wordlist)):
            word = wordlist[i]
            wordIDict[word.lower()].append((i, word))
            
        ret = []
        
        
        def findByReplace(i, q):
            if i >= len(q): 
                return (len(wordlist), \"\")
            
            found = \"\"
            best = len(wordlist)
            if q[i] in VOWELS:
                for c in VOWELS:
                    q[i] = c
                    qword = ''.join(q)
                    if qword in wordIDict:
                        (n, word) = wordIDict[qword][0]
                        if n < best:
                            found = word
                            best = n
                    (n, word) = findByReplace(i+1, q)
                    if n < best:
                        found = word
                        best = n
            else:
                return findByReplace(i+1, q)
            
            return (best, found)

        
        
        for query in queries:
            if query in wordDict:
                ret.append(query)
            elif query.lower() in wordIDict:
                ret.append(wordIDict[query.lower()][0][1])
            else:  
                ret.append(findByReplace(0, list(query.lower()))[1])
            
        return ret
