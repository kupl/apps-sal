class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        original = set(wordlist)
        insensitive = {w.lower(): w for w in reversed(wordlist)}
        vowels = {}
        for c in reversed(wordlist):
            w = c.lower()
            t = w.replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace('u', '_')
            vowels[t] = c
        results = []
        for q in queries:
            if q in original:
                results.append(q)
                continue
            low = q.lower()
            if low in insensitive:
                results.append(insensitive[low])
                continue
            # vowel replace
            t = low.replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace('u', '_')
            if t in vowels:
                results.append(vowels[t])
                continue
            results.append(\"\")
        return results
