class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = dict()
        for name in names:
            d[name] = d.get(name, 0) + 1
            if d[name] > 1:
                i = d[name] - 1
                temp = name + '(' + str(i) + ')'
                while temp in d:
                    i += 1
                    temp = name + '(' + str(i) + ')'
                d[name] = i + 1
                d[temp] = 1
        return d.keys()
