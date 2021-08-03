import math


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = {}
        for i, name in enumerate(keyName):
            t = keyTime[i]
            if name in dic:
                dic[name].append(int(t[0:2] + t[3:]))
            else:
                dic.setdefault(name, [int(t[0:2] + t[3:])])
        alert = []

        def ihan(name):
            timeList = dic[name]
            timeList.sort()
            print(dic[name])
            for t in range(len(timeList) - 2):
                print(math.floor(timeList[t] / 100) * 100)
                if timeList[t + 2] > timeList[t] and timeList[t + 2] - timeList[t] <= 100:
                    return True
            return False
        for name in dic:
            if len(dic[name]) > 2 and ihan(name):
                alert.append(name)
            alert.sort()
        return alert
