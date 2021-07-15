class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic, visit = {}, set()
        res = []
        for i in names:
            if i not in dic and i not in visit:
                dic[i] = 1
                res.append(i)
                visit.add(i)
            else:
                if i not in dic:
                    dic[i] = 1
                while i+\"(\"+str(dic[i])+\")\" in visit:
                    dic[i] += 1
                new = i+\"(\"+str(dic[i])+\")\"
                visit.add(new)
                res.append(new)
                dic[i] += 1
        return res
