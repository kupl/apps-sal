class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        for i in range(len(keyName)):
            h = int(keyTime[i][0:2])
            m = int(keyTime[i][3:5])
            if keyName[i] in d:
                d[keyName[i]].append(h * 60 + m)
            else:
                d[keyName[i]] = [h * 60 + m]
        ans = []
        for k in list(d.keys()):
            if len(d[k]) < 3:
                continue
            else:
                record = d[k]
                record.sort()
                for i in range(len(record) - 2):
                    start = record[i]
                    if record[i + 1] - start <= 60 and record[i + 2] - start <= 60:
                        ans.append(k)
                        break
        ans.sort()
        return ans
