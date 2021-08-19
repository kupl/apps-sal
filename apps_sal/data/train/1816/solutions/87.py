class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def checktime(s1, s2):
            h1 = int(s1.split(':')[0])
            m1 = int(s1.split(':')[1])
            h2 = int(s2.split(':')[0])
            m2 = int(s2.split(':')[1])
            if h2 * 60 + m2 - h1 * 60 - m1 <= 60:
                return True
            else:
                return False
        rec = {}
        for i in range(len(keyName)):
            if keyName[i] in rec:
                rec[keyName[i]].append(keyTime[i])
            else:
                rec[keyName[i]] = [keyTime[i]]
        for i in rec.keys():
            rec[i].sort()
        ans = set()
        for i in rec.keys():
            for j in range(len(rec[i]) - 2):
                if checktime(rec[i][j], rec[i][j + 2]):
                    ans.add(i)
        ans = list(ans)
        ans.sort()
        return ans
