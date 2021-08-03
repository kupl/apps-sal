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

#                 def merge(arr):
#             # base case
#             if len(arr) <= 1:
#                 return arr

#             pivot = int(len(arr)/2)
#             left = merge(arr[:pivot])
#             right = merge(arr[pivot:])

#             return sort(left, right)


#         def sort(left, right):
#             left_cur = right_cur = 0
#             sorted_arr = []
#             while (left_cur < len(left) and right_cur < len(right)):
#                 if left[left_cur] > right[right_cur]:
#                     sorted_arr.append(right[right_cur])
#                     right_cur += 1
#                 else:
#                     sorted_arr.append(left[left_cur])
#                     left_cur += 1

#             sorted_arr += left[left_cur:] + right[right_cur:]

#             return sorted_arr

#         return merge(nums)
