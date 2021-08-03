class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        result = []
        
        name_set = set()
        
        for name in names:
            
            filesystem_name = name
            
            k = 0
            
            while filesystem_name in name_set:
                k += 1
                filesystem_name = f\"{name}({k})\"
            
            name_set.add(filesystem_name)
            
            result.append(filesystem_name)
        
        return result
