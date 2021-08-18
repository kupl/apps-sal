class Solution:
    def commondenominator(self, a, b):
        temp = b
        while(temp > 1):
            if a % temp == 0 and b % temp == 0:
                return temp
            temp -= 1
        return -1

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck or len(deck) < 2:
            return False
        d = dict()
        for x in deck:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        mini = float('inf')
        ret = 1
        for x in d:
            if mini == float('inf'):
                mini = d[x]
                continue
            if d[x] != mini:
                ret = self.commondenominator(d[x], mini)
                if ret < 0:
                    return False
                else:
                    mini = ret
        return True
