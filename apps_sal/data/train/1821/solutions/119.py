class Solution:

    def sortArray(self, listToSort: List[int]) -> List[int]:
        divider = len(listToSort) // 2
        a = listToSort[:divider]
        b = listToSort[divider:]
        sortedList = listToSort[0:len(listToSort)]
        a.sort()
        b.sort()
        i = 0
        j = 0
        k = 0
        while i < len(a) and j < len(b):
            if b[j] < a[i]:
                sortedList[k] = b[j]
                j += 1
                k += 1
            else:
                sortedList[k] = a[i]
                i += 1
                k += 1
        if i < len(a):
            sortedList[k:] = a[i:]
        if j < len(b):
            sortedList[k:] = b[j:]
        listToSort[0:len(listToSort)] = sortedList[0:len(sortedList)]
        return listToSort
