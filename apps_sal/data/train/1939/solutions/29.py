class Solution:

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ww = set(wordlist)
        d = {}
        case = {}
        trs = str.maketrans('aeiou', '*****')
        for w in wordlist:
            r = w.lower()
            if r not in d:
                d[r] = w
            k = r.translate(trs)
            if k not in case:
                case[k] = w
        res = []
        for q in queries:
            if q in ww:
                res.append(q)
            else:
                x = q.lower()
                if x in d:
                    res.append(d[x])
                else:
                    y = x.translate(trs)
                    if y in case:
                        res.append(case[y])
                    else:
                        res.append('')
        return res
