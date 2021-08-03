class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        dic1, dic2, dic3 = {}, {}, {}
        for word in wordlist[::-1]:
            dic1[word] = word
            dic2[word.lower()] = word
            dic3[re.sub('[aeiou]', '*', word.lower())] = word
        return [dic1.get(q) or dic2.get(q.lower()) or dic3.get(re.sub('[aeiou]', '*', q.lower())) or \"\" for q in queries]
        # for q in queries:
        #     if q in dic1:
        #         ans.append(q)
        #         continue
        #     elif q.lower() in dic2:
        #         ans.append(dic2[q.lower()][0])
        #         continue
        #     elif re.sub('[aeiou]', '*', q.lower()) in dic3:
        #         ans.append(dic3[re.sub('[aeiou]', '*', q.lower())][0])
        #     else:
        #         ans.append(\"\")
        # # print(dic3)
        # return ans
