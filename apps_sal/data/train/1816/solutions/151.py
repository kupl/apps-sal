class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        x = defaultdict(list)
        for i in range(len(keyName)):
            time = int(keyTime[i][0:2] + keyTime[i][3:5])
            x[keyName[i]].append(time)
        threePeat = []
        for (key, value) in list(x.items()):
            if len(value) >= 3:
                value = sorted(value)
                for i in range(len(value) - 2):
                    if value[i + 1] - 100 <= value[i] and value[i + 2] - 100 <= value[i]:
                        threePeat.append(key)
                        break
        return sorted(threePeat)
