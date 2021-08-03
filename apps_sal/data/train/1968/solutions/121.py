class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        x = sorted(folder)
        res = [x[0]]
        for i in range(1, len(x)):
            if x[i].startswith(res[-1]) and (x[i][len(res[-1])] == '/'):
                continue
            res.append(x[i])
        return res
