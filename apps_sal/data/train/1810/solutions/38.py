class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        result = []
        
        name_count = {}

        for name in names:
            k = name_count.get(name,0)
            
            fs_name = name
            
            if k > 0:
                
                while fs_name in name_count:
                    fs_name = f\"{name}({k})\"
                    k += 1
    
                name_count[fs_name] = 1
                name_count[name] = k
            else:
                name_count[name] = 1
                
            result.append(fs_name)
                
                
            
            
        return result
