class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return []
        folder.sort()
        result = [folder[0]]
        for f in folder:
            if f != result[-1] and not f.startswith(result[-1] + \"/\"):
                result.append(f)
        return result
                
            
            
        
