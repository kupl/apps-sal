class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return None
        folder.sort(key=lambda x: len(x))
        seen = set()
        for fold in folder:
            for i in range(2, len(fold)):
                if fold[i] == '/' and fold[:i] in seen:
                    break
            else:
                seen.add(fold)
        return list(seen)
