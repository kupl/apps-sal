class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # for i in range(len(wordlist)):
        #     if wordlist[i] != queries[i]:
        #         print(i,wordlist[i], queries[i])
        #         break

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

#         low_origin, wild_origin = collections.defaultdict(str), collections.defaultdict(str)
#         s = set(wordlist)
#         def to_wild(word): return ''.join(['*' if c in 'aeiou' else c for c in word])

#         for word in wordlist:
#             low = word.lower()
#             if low not in low_origin: low_origin[low] = word
#             wild = to_wild(low)
#             if wild not in wild_origin: wild_origin[wild] = word
#         print()
#         ans = []
#         for query in queries:
#             low = query.lower()
#             wild = to_wild(low)
#             if query in s: ans.append(query)
#             elif low in low_origin: ans.append(low_origin[low])
#             elif wild in wild_origin: ans.append(wild_origin[wild])
#             else: ans.append('')
#         return ans
