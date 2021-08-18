class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        n = len(keyName)
        res = []
        keyTime, keyName = list(zip(*sorted(zip(keyTime, keyName))))
        for i in range(n):
            if keyName[i] not in d:
                d[keyName[i]] = [keyTime[i], [0], [0], True, False]
            else:
                if not d[keyName[i]][4]:
                    min_diff = int(str(keyTime[i][3:])) - int(str(d[keyName[i]][0][3:]))
                    hr_diff = int(str(keyTime[i][:2])) - int(str(d[keyName[i]][0][:2]))

                    if min_diff < 0:
                        min_diff = 60 + min_diff
                        hr_diff = hr_diff - 1
                    if hr_diff < 0:
                        d[keyName[i]] = [keyTime[i], [0], [0], True, False]
                    else:
                        d[keyName[i]][0] = keyTime[i]
                        d[keyName[i]][1].append(hr_diff * 60 + min_diff)
                        d[keyName[i]][2].append(d[keyName[i]][1][-1] + d[keyName[i]][1][-2])

                        if len(d[keyName[i]][2]) > 2 and d[keyName[i]][2][-1] <= 60:
                            d[keyName[i]][4] = True
                            res.append(keyName[i])
        return sorted(res)
