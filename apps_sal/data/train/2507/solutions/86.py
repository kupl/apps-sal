class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for i in chars:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = 0
        for i in words:
            flag = True
            for j in i:
                if j in d:
                    if i.count(j) > d[j]:
                        flag = False
                else:
                    flag = False
            if flag:
                l += len(i)
        return l
