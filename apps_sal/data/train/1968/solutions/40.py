class Solution:

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        seen = set()
        folders.sort(key=lambda x: len(x))
        for folder in folders.copy():
            folder_split = folder.split('/')[1:]
            for i in range(len(folder_split)):
                if tuple(folder_split[:i + 1]) in seen:
                    folders.remove(folder)
                    break
            else:
                seen.add(tuple(folder_split))
        return folders
