class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def check(f):
            return all(map(lambda x: len(x) > 0, f.split('/')[1:]))

        def parent(f):
            parents = set()
            tmp = f.split('/')
            for i in range(1, len(tmp) - 1):
                parents.add('/'.join(tmp[:i + 1]))
            return parents
        folder.sort()
        seen = set()
        res = []
        for f in folder:
            if check(f):
                flag = False
                ps = parent(f)
                for p in ps:
                    if p in seen:
                        flag = True
                        break
                if not flag:
                    res.append(f)
                seen.add(f)
        return res
