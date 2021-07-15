class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_subs = []
        folder_k = sorted(folder, key=len)
        for f in folder_k:
            flag = False
            for j in folder_subs:
                if f.startswith(j + '/'):
                    flag = True
                    break
            if not flag:
                folder_subs.append(f)
                    
        return folder_subs
