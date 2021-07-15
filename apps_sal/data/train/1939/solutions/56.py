class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def generate(string):
            if not string:
                yield string
            else:
                if string[0] in vowel:
                    for v in vowel:
                        for g in generate(string[1:]):
                            yield v + g
                else:
                    for g in generate(string[1:]):
                        yield string[0] + g
        
        dicti, vowel, ans = {}, {\"a\", \"e\", \"i\", \"o\", \"u\"}, []
        for word in wordlist:
            cur = word.lower()
            if cur not in dicti:
                dicti[cur] = [set(), None, None]
            dicti[cur][0].add(word)
            if dicti[cur][1] is None:
                dicti[cur][1] = word
            for new in generate(cur):
                if new not in dicti:
                    dicti[new] = [set(), None, None]
                if dicti[new][2] is None:
                    dicti[new][2] = word
        for query in queries:
            cur, flag = query.lower(), 1
            if cur in dicti:
                if query in dicti[cur][0]:
                    ans.append(query)
                    flag = 0
                elif dicti[cur][1] is not None:
                    ans.append(dicti[cur][1])
                    flag = 0
            if flag:
                for new in generate(cur):
                    if new in dicti and dicti[new][2] is not None:
                        ans.append(dicti[new][2])
                        flag = 0
                        break
            if flag:
                ans.append(\"\")
        return ans
