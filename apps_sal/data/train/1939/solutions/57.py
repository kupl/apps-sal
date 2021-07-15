class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        first = set(wordlist)
        second = [word.lower() for word in wordlist]
        third = []
        for word in wordlist:
            tmp = \"\"
            for c in word:
                if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                    tmp += c
                else:
                    tmp += 'a'
            third.append(tmp.lower())
        res = []
        for query in queries:
            if query in first:
                res.append(query)
                continue
            try:
                idx = second.index(query.lower())
                res.append(wordlist[idx])
                continue
            except ValueError:
                pass
            vowelIns = \"\"
            for c in query:
                if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                    vowelIns += c
                else:
                    vowelIns += 'a'
            try:
                idx = third.index(vowelIns.lower())
                res.append(wordlist[idx])
            except ValueError:
                res.append(\"\")
        return res
