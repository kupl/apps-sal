import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def vowel_norm(inword):
            return re.sub(r\"[aeiou]\", \"a\", inword)

        lookup_lower, lookup_vowel = {}, {}
        for w in wordlist:
            l = w.lower()
            lookup_lower[l] = lookup_lower.get(l, []) + [w]
            lv = vowel_norm(l)
            lookup_vowel[lv] = lookup_vowel.get(lv, []) + [w]
        wordlist = set(wordlist)

        res = []
        for q in queries:
            qlow = q.lower()
            qvowel = vowel_norm(qlow)
            if q in wordlist:
                res.append(q)
            elif qlow in lookup_lower:
                res.append(lookup_lower[qlow][0])
            elif qvowel in lookup_vowel:
                res.append(lookup_vowel[qvowel][0])
            else:
                res.append(\"\")
        return res
