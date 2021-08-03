class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tmp = '*'
        res = []
        for elem in sorted(folder):
            if not elem.startswith(tmp):
                tmp = elem + '/'
                res.append(elem)
        return res
