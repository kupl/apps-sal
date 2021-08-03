class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ht = {}
        res = OrderedDict()

        for name in names:
            if name not in ht:
                ht[name] = 1

            if name not in res:
                res[name] = True
                continue

            key = name + '(' + str(ht[name]) + ')'
            while key in res:
                ht[name] += 1
                key = name + '(' + str(ht[name]) + ')'

            res[key] = True

        return res
