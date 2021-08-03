class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        if not names: return []
        res = []
        dic = {}
        for name in names:
            if name not in dic:
                res.append(name)
                dic[name] = 1
            else:
                k = dic[name]
                while \"{}({})\".format(name, k) in dic:
                    k += 1
                modname = \"{}({})\".format(name, k)
                dic[name] = k+1
                dic[modname] = 1
                res.append(modname)
        return res
                
