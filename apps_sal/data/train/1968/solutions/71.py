class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [ folder[0]]
        prev = folder[0] + '/'
        for f in folder[1:]:
            if not f.startswith(prev):
                ans.append(f)
                prev = f+'/'
        return ans
