class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:

        folders.sort()
        first = folders[0]
        res_set = set()
        res_set.add(first)
        for i in range(1, len(folders)):
            folder = folders[i]
            if folder.startswith(first) and folder.count('/') > first.count('/'):
                pass
            else:
                res_set.add(folder)
                res_set.add(first)
                first = folder

        res = list(res_set)
        res.sort()
        return res
