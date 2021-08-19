class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        a = set()
        b = []
        for i in names:
            if i in a:
                k = 1
                s = f'{i}({k})'
                while s in a:
                    k += 1
                    s = f'{i}({k})'
                a.add(s)
                b.append(s)
            else:
                a.add(i)
                b.append(i)
        return b
