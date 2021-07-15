class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        folder_set = set(folder)
        
        n = len(folder)
        prev = folder[0]
        
        i = 1
        while i < n:
            curr = folder[i]
            
            len_prev, len_curr = len(prev), len(curr)
            if len_prev < len_curr:
                if curr[:len_prev] in folder_set:
                    if curr[len_prev] == '/':
                        folder.remove(curr)
                        curr = prev
                        i-= 1
                        n-= 1
                            
            prev = curr
            i+= 1
        
        return folder
