class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(ls1, ls2):
            i = j = 0
            sortedList = []
            while i < len(ls1) and j < len(ls2):
                if ls1[i] < ls2[j]:
                    sortedList.append(ls1[i])
                    i += 1
                else:
                    sortedList.append(ls2[j])
                    j += 1
            if i < len(ls1):
                sortedList += ls1[i:]
            else:
                sortedList += ls2[j:]
            return sortedList

        def divide(ls):
            if len(ls) <= 1:
                return ls
            middle = int(len(ls) / 2)
            ls1 = divide(ls[:middle])
            ls2 = divide(ls[middle:])
            return sort(ls1, ls2)
        return divide(nums)
