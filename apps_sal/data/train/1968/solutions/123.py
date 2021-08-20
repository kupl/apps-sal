class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        res = []
        seen = set()
        for path in folder:
            tmp = []
            for d in path.split('/')[1:]:
                tmp.append(d)
                if '/'.join(tmp) in seen:
                    break
            else:
                seen.add('/'.join(tmp))
                res.append(path)
        return res
