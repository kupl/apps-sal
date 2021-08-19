class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if len(folder) == 1:
            return folder
        folder.sort()
        i = 0
        while i < len(folder) - 1:
            if folder[i + 1].startswith(folder[i] + '/'):
                folder.pop(i + 1)
            else:
                i += 1
        return folder
