class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        for i in range(len(keyName)):
            if keyName[i] in d:
                d[keyName[i]].append(keyTime[i])
            else:
                d[keyName[i]] = [keyTime[i]]
        e = []
        for i in d:
            c = []
            for j in d[i]:
                c.append(int(j[0]) * 600 + int(j[1]) * 60 + int(j[3] + j[4]))
            c.sort()
            if(len(c) <= 2):
                continue
            else:
                for k in range(2, len(c)):
                    if(c[k] - c[k - 2] <= 60):
                        e.append(i)
                        break
        e.sort()
        return e
