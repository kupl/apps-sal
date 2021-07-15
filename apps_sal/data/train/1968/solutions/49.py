class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        dirs = set()
        folders = sorted(list(filter(None,folder.split('/'))) for folder in folders)
        
        print(folders)
        
        for folder_fp in folders:
            curr_name = \"\"
            for folder in folder_fp:
                curr_name += f\"/{folder}\"
                if curr_name in dirs:
                    break
            else:
                dirs.add(curr_name)
            #print(dirs)
        return dirs
