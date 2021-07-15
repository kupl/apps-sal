class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        n = len(folder)
        prev = folder[0]
        
        i = 1
        while i < n:
            curr = folder[i]
            
            if curr.startswith(prev + '/'):
                folder.remove(curr)
                curr = prev
                i-= 1
                n-= 1
                            
            prev = curr
            i+= 1
        
        return folder
