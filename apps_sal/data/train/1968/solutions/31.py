class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        res = [folder.pop(0)]
        n = len(folder)

        for i in range(n):
            pattern = f'^{res[-1]}/'
            result = re.match(pattern, folder[i])
            if not result:
                res += [folder[i]]

        return res
