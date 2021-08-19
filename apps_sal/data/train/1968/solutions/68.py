class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        seen = set(folder)
        for i in folder:
            path = i
            while path:
                path = path[:path.rfind('/')]
                if path in seen:
                    break
            else:
                ans.append(i)
        return ans
