class Solution:
    def within_hour(self, t1, t2):
        hh1, ss1 = list(map(int, t1.split(':')))
        hh2, ss2 = list(map(int, t2.split(':')))
        hdiff = hh2 - hh1
        if hdiff > 1 or hdiff < 0:
            return False
        sdiff = ss2 - ss1
        return (hdiff * 60 + sdiff) <= 60

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        d = {}
        result = set()
        for kn, kt in zip(keyName, keyTime):
            if kn in d:
                d[kn].append(kt)
            else:
                d[kn] = [kt]
        result = []
        for k, v in list(d.items()):
            v.sort(key=lambda x: tuple(map(int, x.split(':'))))
            for i in range(len(v) - 2):
                if self.within_hour(v[i], v[i + 2]):
                    result.append(k)
                    break
        return sorted(result)
