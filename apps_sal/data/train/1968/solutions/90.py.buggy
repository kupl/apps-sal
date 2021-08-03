class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        
        folders_set = set(folder)
        res = []
        # print(folders, \"/a\" in folders)
        
        
        for folder_and_subfolder in folder:
            
            folders = folder_and_subfolder.split('/')[1:]
            print(folders)
            
            i = 0 
            subfolder = \"/\"
            flag = False
            while i < len(folders):
                
                subfolder = subfolder + str(folders[i]) 
                # print((subfolder), str(subfolder) in folders_set)
                if subfolder in folders_set:
                    flag = True
                    res.append(subfolder)
                    break
                subfolder += \"/\"
                
                i+=1
            if not flag:
                res.append(subfolder)
                
            
        return list(set(res))
                
            
            
