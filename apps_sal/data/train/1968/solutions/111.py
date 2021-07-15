class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        for f in sorted(folder):
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res
        # res = []
        # folder.sort(key = lambda x: len(x))
        # seen = set()
        # for f in folder:
        #     if not any(f[i] == '/' and f[:i] in seen for i in range(2, len(f))):
        #         seen.add(f)
        # return list(seen)

