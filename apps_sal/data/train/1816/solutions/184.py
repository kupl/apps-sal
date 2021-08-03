class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        pairs = []

        for i in range(len(keyName)):
            pairs.append((keyName[i], self.getMinutes(keyTime[i])))
        pairs.sort()

        print(pairs)

        i = 0
        res = []
        while i + 2 < len(pairs):
            if pairs[i + 2][0] == pairs[i][0]:
                name = pairs[i][0]
                print(name)
                print(pairs[i + 1][1], pairs[i][1] + 60)
                print(pairs[i + 2][1], pairs[i][1] + 60)
                if pairs[i + 1][1] <= pairs[i][1] + 60 and pairs[i + 2][1] <= pairs[i][1] + 60:
                    res.append(pairs[i][0])
                    while i < len(pairs) and pairs[i][0] == name:
                        i += 1
                    i -= 1
            i += 1
        return res

    def getMinutes(self, time):
        hh, mm = time.split(':')
        return int(hh) * 60 + int(mm)
