class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        seen = set()
        folders.sort(key=lambda x: len(x))
        for folder in folders.copy():
            for i in range(2, len(folder)):
                if folder[i] == '/' and folder[:i] in seen:
                    folders.remove(folder)
                    break
            else:
                seen.add(folder)

        return folders
