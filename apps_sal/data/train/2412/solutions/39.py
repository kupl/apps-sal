from itertools import groupby


class Solution:
    def removeDuplicates(self, S: str) -> str:

        uncompleted = True
        while uncompleted:
            uncompleted = False
            tmp = ['']
            for key, grp in groupby(S):
                letters = list(grp)
                if len(letters) == 1:
                    tmp.extend(letters)
                else:
                    tmp.append(key * (len(letters) - 2))
                    uncompleted = True
            S = ''.join(tmp)
        return S
