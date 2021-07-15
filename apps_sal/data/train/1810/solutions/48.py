class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        if not names: return []
        ans = []
        dic = {}
        for name in names:
            if name not in dic:
                ans.append(name)
                dic[name] = 1
            else:
                k = dic[name]
                while \"{}({})\".format(name, k) in dic:
                    k += 1
                dic[name] = k+1
                name = \"{}({})\".format(name, k)
                dic[name] = 1
                ans.append(name)
            
        return ans
        
