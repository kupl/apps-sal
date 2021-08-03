class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        checker = {}
        l = len(keyName)
        for i in range(l):
            if keyName[i] not in checker:
                checker[keyName[i]] = [keyTime[i]]
            else:
                checker[keyName[i]].append(keyTime[i])
        ans = []
        for a, b in checker.items():
            l = len(b)
            if l > 2:
                b.sort()
                for i in range(l - 2):
                    t = b[i].split(':')
                    t = str(int(t[0]) + 1) + ':' + t[1]
                    if len(t) == 4:
                        t = '0' + t
                    if t >= b[i + 2]:
                        ans.append(a)
                        break
        ans.sort()
        return ans
