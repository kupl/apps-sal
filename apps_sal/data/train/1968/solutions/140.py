class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x: len(x))

        hashmap = set()

        for f in folder:
            seen = False
            for i in range(2, len(f)):
                if f[i] == \"/\" and f[:i] in hashmap:
                    seen = True
                    break
            
            if not seen: hashmap.add(f)

        return hashmap
        
