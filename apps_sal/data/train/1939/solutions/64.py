class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        lw = {}
        for i in wordlist:
            if i.lower() not in lw:
                lw[i.lower()] = i
        vfw = {}
        for j in wordlist:
            if re.sub('[aeiou]', '*', j.lower()) not in vfw:
                vfw[re.sub('[aeiou]', '*', j.lower())] = j
        l = len(queries)
        res = []
        for i in range(l):
            low = queries[i].lower()
            wild = ''.join(['*' if i in 'aeiou' else i for i in low])
            if queries[i] in wordlist:
                res.append(queries[i])
                continue
            elif low in lw:
                res.append(lw[low])
            elif wild in vfw:
                res.append(vfw[wild])
            else:
                res.append('')
        return res
