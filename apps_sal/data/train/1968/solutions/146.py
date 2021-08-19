class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dic = set(folder)
        for x in folder:
            for i in range(len(x)):
                if i != 0 and x[i] == '/':
                    if x[:i] in dic:
                        dic.remove(x)
                        break
        return list(dic)
