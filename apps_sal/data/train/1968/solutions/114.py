class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        pfix = set()
        removed = set()
        for f in folder:
            valid = f.split('/')
            for i in range(0, len(valid)):
                target = '/'.join(valid[0:i + 1])
                if target in pfix:
                    removed.add(f)
            pfix.add(f)
        return set(folder) - set(removed)
