class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_subs = []
        folder.sort(key=len)
        for f in folder:
            flag = False
            for j in folder_subs:
                if f.startswith(j + '/'):
                    flag = True
                    break
            if not flag:
                folder_subs.append(f)

        return folder_subs
