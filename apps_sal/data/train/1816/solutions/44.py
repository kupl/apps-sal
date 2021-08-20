class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        out = []
        freq = {}
        alerts = {}
        for i in range(len(keyName)):
            seconds = int(keyTime[i][:2]) * 60 + int(keyTime[i][-2:])
            if keyName[i] in alerts:
                alerts[keyName[i]].append(seconds)
            else:
                alerts[keyName[i]] = [seconds]
                freq[keyName[i]] = 0
        print(alerts)
        for (name, time) in list(alerts.items()):
            for i in range(len(time) - 2):
                time = sorted(time)
                if time[i + 1] - time[i] <= 60 and time[i + 2] - time[i] <= 60:
                    freq[name] += 1
        print(freq)
        for (name, _) in list(freq.items()):
            if freq[name] >= 1:
                out.append(name)
        return sorted(out)
