class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        n = len(names)
        dic = {}
        for i in range(n):
            name = names[i]
            if name not in dic:
                dic[name] = 0
            else:
                k = dic[name] + 1
                while True:
                    temp = name + \"(\" + str(k) + \")\"
                    if temp not in dic:
                        dic[temp] = 0
                        dic[name] = k
                        break
                    k += 1
                names[i] = temp
        return names
