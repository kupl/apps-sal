class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = {}
        res = set()

        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]

            if name not in dic:
                dic[name] = []

            time = list(map(int, time.split(':')))

            time = time[0] + time[1] / 60
            dic[name].append(time)

        for name in dic:
            t = sorted(dic[name])
            if len(t) >= 3:
                for j in range(len(t) - 2):
                    if t[j + 2] - t[j] <= 1.0001:
                        res.add(name)

        return sorted(list(res))
