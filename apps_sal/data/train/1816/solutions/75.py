class Solution:

    def timediff(self, t1, t2):
        hdiff = int(t2[:2]) - int(t1[:2])
        mdiff = int(t2[-2:]) - int(t1[-2:])
        fdiff = hdiff * 60 + mdiff
        return fdiff

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = dict()
        for i in range(len(keyName)):
            if keyName[i] in list(times.keys()):
                times[keyName[i]].append(keyTime[i])
            else:
                times[keyName[i]] = [keyTime[i]]
        bad = set()
        for name in list(times.keys()):
            t = sorted(times[name])
            for i in range(2, len(t)):
                if self.timediff(t[i - 2], t[i]) <= 60:
                    bad.add(name)
                    break
        return sorted(list(bad))
