class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder, key=lambda e: len(e))
        res = set()
        for f in folder:
            flag = True
            for i in range(2, len(f)):
                if f[i] == '/' and f[:i] in res:
                    flag = False
                    break
            if flag:
                res.add(f)
        return list(res)
