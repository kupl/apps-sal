class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        dic = dict()
        for i in range(len(names)):
            if names[i] not in dic:
                dic[names[i]] = 1
                ans.append(names[i])
            else:
                name = names[i]+\"(\"+str(dic[names[i]])+\")\"
                while name in dic:
                    dic[names[i]] += 1
                    name = names[i]+\"(\"+str(dic[names[i]])+\")\"
                dic[name] = 1
                ans.append(name)
        return ans
