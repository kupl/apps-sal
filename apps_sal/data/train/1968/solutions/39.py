class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        seen = set()
        # folders.sort(key = lambda x: len(x.split('/')))
        folders.sort(key = lambda x: len(x))
        # print(folders)
        for folder in folders.copy():
            # print(folder)
            # folder_split = folder.split('/')[1:]
            for i in range(2, len(folder)):
                if folder[i] == '/' and folder[:i] in seen: 
                    folders.remove(folder)
                    break
            else: seen.add(folder)
            # print(seen)
                    
        return folders
