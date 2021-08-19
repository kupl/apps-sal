class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keys = {}
        for i in range(len(keyName)):
            if keyName[i] in keys:
                keys[keyName[i]].append(keyTime[i])
            else:
                keys[keyName[i]] = [keyTime[i]]

        res = []
        for i in keys.keys():
            time = keys[i]
            if self.emitAlert(time):
                res.append(i)

        return sorted(res)

    def emitAlert(self, t: List[str]) -> bool:
        time_converted = []
        for i in t:
            t = i.split(':')
            time_converted.append(60 * int(t[0]) + int(t[1]))
        time_converted.sort()

        left = 0
        # print(time_converted)
        for i in range(len(time_converted)):
            while time_converted[i] - time_converted[left] > 60:
                left += 1
            if i > 0 and time_converted[i] < time_converted[i - 1]:
                left = i
            if i - left >= 2:
                return True

        return False
