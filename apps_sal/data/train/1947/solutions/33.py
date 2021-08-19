class Solution:

    def issubset(self, s: str, t: str) -> bool:
        dic = dict()
        for i in range(len(t)):
            dic[t[i]] = dic.get(t[i], 0) + 1
        result = True
        i = 0
        while i < len(s) and result:
            if s[i] not in list(dic.keys()) or dic[s[i]] < 1:
                result = False
            else:
                dic[s[i]] -= 1
                i += 1
        return result

    def joining(self, B: List[str]) -> str:
        result = dict()
        for i in range(len(B)):
            word = B[i]
            temp = dict()
            for j in range(len(word)):
                temp[word[j]] = temp.get(word[j], 0) + 1
            for (k, v) in list(temp.items()):
                if k not in list(result.keys()) or result[k] < v:
                    result[k] = v
        res = ''
        for (k, v) in list(result.items()):
            res += k * v
        return res

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        union = self.joining(B)
        for word in A:
            if self.issubset(union, word) == True:
                res.append(word)
        return res
