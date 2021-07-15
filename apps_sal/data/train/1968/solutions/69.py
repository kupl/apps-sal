class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        seen = set()
        folder.sort(key=len)
        
        for fd in folder:
            for i in range(2, len(fd)):
                if fd[i] == \"/\":
                    if fd[:i] in seen:
                        break
            else:
                seen.add(fd)
                
        return list(seen)
                
                        
                        
                    
                
        
