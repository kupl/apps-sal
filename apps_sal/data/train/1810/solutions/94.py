class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        m = set()
        m2 = dict()
        f = []
        for x in names:
            if x not in m:
                m.add(x)
                f.append(x)
                m2[x] = 1
            elif x in m2:
                while x + '(' + str(m2[x]) + ')' in m:
                    m2[x] += 1
                m.add(x + '(' + str(m2[x]) + ')')
                f.append(x + '(' + str(m2[x]) + ')')
            else:
                m2[x] = 1
                while x + '(' + str(m2[x]) + ')' in m:
                    m2[x] += 1
                m.add(x + '(' + str(m2[x]) + ')')
                f.append(x + '(' + str(m2[x]) + ')')
        return f
