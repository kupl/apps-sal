class Solution:

    def sortArray(self, listToSort: List[int]):
        if len(listToSort) == 0 or len(listToSort) == 1:
            return listToSort
        elif len(listToSort) == 2:
            if listToSort[0] > listToSort[1]:
                (listToSort[0], listToSort[1]) = (listToSort[1], listToSort[0])
        else:
            divider = len(listToSort) // 2
            l = listToSort[:divider]
            r = listToSort[divider:]
            self.sortArray(l)
            self.sortArray(r)
            i = 0
            j = 0
            k = 0
            while i < len(l) and j < len(r):
                if r[j] < l[i]:
                    listToSort[k] = r[j]
                    j += 1
                    k += 1
                else:
                    listToSort[k] = l[i]
                    i += 1
                    k += 1
            if i < len(l):
                listToSort[k:] = l[i:]
            if j < len(r):
                listToSort[k:] = r[j:]
        return listToSort
