class Solution:

    def getFolderNames(self, names):
        res = []
        allname = collections.Counter()
        for name in names:
            if name in allname:
                while f'{name}({allname[name]})' in allname:
                    allname[name] += 1
                res.append(f'{name}({allname[name]})')
                allname[f'{name}({allname[name]})'] = 1
            else:
                allname[name] = 1
                res.append(name)
        return res
