class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dicts = {}
        res = []
        folder.sort(key=lambda x: len(x))
        for fo in folder:
            candidates = []
            for i in range(len(fo)):
                if fo[i] == '/':
                    candidates.append(i)
            candidates = candidates[1:]
            candidates.append(len(fo))
            add = True
            for can in candidates:
                if fo[:can] in dicts:
                    add = False
                    break
            if add:
                res.append(fo)
                dicts[fo] = 1
        return res
