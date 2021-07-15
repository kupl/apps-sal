class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        for name in names:
            if name not in d:
                d[name] = 1
                new_name = name
            else:
                k = d[name]
                while name + '(' + str(k) + ')' in d:
                    k += 1
                new_name= name + '(' + str(k) + ')'
                d[name] = k
                d[new_name] = 1
            res.append(new_name)
        return res
