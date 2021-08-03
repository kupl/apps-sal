class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sort = sorted(folder, key = len)
        
        visited = []
        
        for f in sort:
            found = False
            for prefix in visited:
                if f.startswith(prefix + \"/\"):
                    found = True
                    break
            if not found:
                visited.append(f)
        return visited
