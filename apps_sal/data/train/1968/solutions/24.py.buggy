class Solution:
    
    def is_subfolder(self, parent, current):
        if parent == \"\":
            return False
        
        splitted = current.split(parent)
        
        if len(splitted) == 1:
            return False
        
        if splitted[0] == \"\":
            if splitted[1] == \"\":
                return True
            elif len(splitted[1]) > 0:
                if splitted[1][0] == \"/\":
                    return True
        return False
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        parent = folder[0]
        
        output = []
        output.append(parent)
        
        index  = 1
        
        while(index < len(folder)):
            current = folder[index]
            
            if not self.is_subfolder(parent, current):
                output.append(current)
                parent = current
            
            index += 1
        return output
