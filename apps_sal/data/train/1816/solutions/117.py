import re


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keyCards = {}
        for i in range(len(keyName)):
            if keyName[i] not in keyCards:
                keyCards[keyName[i]] = []
            hour = int(keyTime[i][0:2])
            minute = int(keyTime[i][3:])
            keyCards[keyName[i]].append(hour * 60 + minute)
        alert_names = []
        for key in list(keyCards.keys()):
            my_times = sorted(keyCards[key])
            for i in range(len(my_times) - 2):
                count = 0
                for j in range(i, len(my_times)):
                    if my_times[j] - my_times[i] <= 60:
                        count += 1
                if count >= 3:
                    alert_names.append(key)
                    break
        print(keyCards)
        return sorted(alert_names)
