class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for i in range(len(chars)):
            if chars[i] not in d:
                d[chars[i]] = 1
            else:
                d[chars[i]] += 1
        c = 0
        for i in range(len(words)):
            di = {}
            for j in range(len(words[i])):
                if words[i][j] not in di:
                    di[words[i][j]] = 1
                else:
                    di[words[i][j]] += 1
            l = list(di.keys())
            temp = 0
            for j in range(len(l)):
                if l[j] not in d:
                    temp = 1
                    break
                elif di[l[j]] > d[l[j]]:
                    temp = 1
                    break
                else:
                    temp = 0
            if temp == 0:
                c += len(words[i])
        return c
