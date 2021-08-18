class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        cache = {}
        words = set()
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for w in wordlist:
            words.add(w)

            if w not in cache:
                cache[w] = w

            lowercase = w.lower()
            if lowercase not in cache:
                cache[lowercase] = w

            imd_w = lowercase
            for i, ch in enumerate(w):
                if ch.lower() in vowels:
                    imd_w = imd_w[:i] + '*' + imd_w[i + 1:]
            if imd_w not in cache:
                cache[imd_w] = w

        res = []
        for q in queries:
            if q in words:
                res.append(q)
            else:
                lowercase = q.lower()
                if lowercase in cache:
                    res.append(cache[lowercase])
                else:
                    imd_w = lowercase
                    for i, ch in enumerate(q):
                        if ch.lower() in vowels:
                            imd_w = imd_w[:i] + '*' + imd_w[i + 1:]
                    if imd_w in cache:
                        res.append(cache[imd_w])
                    else:
                        res.append('')
        return res
