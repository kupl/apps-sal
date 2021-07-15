class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        seen = set()
        # folders.sort(key = lambda x: len(x.split('/')))
        folders.sort(key = lambda x: len(x))
        # print(folders)
        for folder in folders.copy():
            # print(folder)
            folder_split = folder.split('/')[1:]
            for i in range(len(folder_split)):
                if tuple(folder_split[:i+1]) in seen: 
                    folders.remove(folder)
                    break
            else: seen.add(tuple(folder_split))
            # print(seen)
                    
        return folders
