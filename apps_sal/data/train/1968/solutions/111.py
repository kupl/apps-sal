class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        for f in sorted(folder):
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res
