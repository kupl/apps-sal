class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        h = {}
        res = []
        for i in names:

            if i not in h:
                h[i] = 0
                res.append(i)
            else:

                h[i] += 1
                new_s = i + \"(\" + (str(h[i])) + \")\"
                while new_s in h:
                    h[i] += 1
                    new_s = i + \"(\" + (str(h[i])) + \")\"
                h[new_s] = 0 
                res.append(new_s)
        return res
