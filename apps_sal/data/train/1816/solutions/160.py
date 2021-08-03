class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for i in range(len(keyName)):
            time = int(keyTime[i][:2] + keyTime[i][3:5])
            times[keyName[i]].append(time)

        print(times)
        threes = []
        for key, value in times.items():
            if len(value) >= 3:
                value = sorted(value)
                for i in range(len(value) - 2):
                    if (value[i + 1] - 100) <= value[i] and (value[i + 2] - 100) <= value[i]:
                        threes.append(key)
                        break
        return sorted(threes)
