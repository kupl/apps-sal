class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        d = {}
        for f in folder:
            names = ''.join(f.split('/'))
            if len(names) > 0:
                d[names] = f

        output = []
        for f in folder:
            names = ''.join(f.split('/')[:-1])
            if not [True for i in range(len(names)) if names[:i + 1] in d]:
                output.append(f)

        return output
