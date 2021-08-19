class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))
        seen = set()
        for f in folder:
            for i in range(2, len(f)):
                if f[i] == '/' and f[:i] in seen:
                    break
            else:
                seen.add(f)
        return list(seen)
