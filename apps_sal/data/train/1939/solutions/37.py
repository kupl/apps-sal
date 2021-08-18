class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def rmvowel(word, iskeepcase=True):
            outword = ''
            word2 = word if iskeepcase else word.lower()
            for char in word2:
                if char in 'aeiou':
                    outword += ' '
                else:
                    outword += char
            return outword

        wordhash = defaultdict(list)
        for word in wordlist:
            wordhash[(word, 1)] = ''
            wordhash[(word.lower(), 2)].append(word)
            wordhash[(rmvowel(word, False), 3)].append(word)

        outq = []
        for query in queries:
            if (query, 1) in wordhash:
                outq.append(query)
            elif (query.lower(), 2) in wordhash:
                outq.append(wordhash[(query.lower(), 2)][0])
            elif (rmvowel(query, False), 3) in wordhash:
                outq.append(wordhash[(rmvowel(query, False), 3)][0])
            else:
                outq.append('')
        return outq
