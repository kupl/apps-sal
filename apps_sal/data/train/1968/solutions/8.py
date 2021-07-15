class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        def get_key(f):
            
            for i in range(len(f) - 1, -1 , -1):
                if(f[i] == \"/\"):
                    return i
            raise Exception
        
        folder = sorted(folder, key=lambda x : len(x))
        top_level_folders = {}
        
        for f in folder:
            
            key = get_key(f)
            parent = f[0:key]
            check = False
            while(parent):
                
                if(parent in top_level_folders):
                    check = True
                key = get_key(parent)
                parent = f[0:key]
            
            if(not check):
                top_level_folders[f] = True
            
            
            
        ret = []
        for key in top_level_folders:
            ret.append(key)
        return ret
