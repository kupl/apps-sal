class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = set()
        folder.sort(key = len)
        for fold in folder:
            flag = 0
            for i in range(2, len(fold)):
                if fold[i] == '/':
                    if fold[:i] in res:
                        flag = 1
                        break
            if flag == 0: res.add(fold)
        return list(res)
