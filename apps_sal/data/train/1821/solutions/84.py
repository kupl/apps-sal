class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''method 1: mergesort (divide and conqueer). Time complexity: T(n) = 2*T(n/2)+O(n) --> TC: O(nlogn). Space complexity: O(n+logn), since the recursion depth is logn, and we allocate size n temporary array to store intermediate results.'''
#         def helper(l,r):
#             if l+1>=r: return
#             m = l + (r-l)//2
#             helper(l, m)
#             helper(m, r)
#             it1 = l
#             it2 = m
#             ind = 0
#             while it1 < m or it2 < r:
#                 if it2 == r or (it1 < m and nums[it1] <= nums[it2]):
#                     temp[ind] = nums[it1]
#                     it1 += 1
#                 else:
#                     temp[ind] = nums[it2]
#                     it2 += 1
#                 ind += 1
#             nums[l:r] = temp[:ind]

#         temp = [0]*len(nums)
#         helper(0, len(nums))
#         return nums
        '''method2: quick sort. not stable. O(nlogn)/O(1)'''
        def pivot(l, r):
            if l >= r:
                return
            p = nums[random.randint(l, r)]
            it1 = l
            it2 = r
            while it1 <= it2:
                while nums[it1] < p:
                    it1 += 1
                while nums[it2] > p:
                    it2 -= 1
                if it1 <= it2:
                    nums[it1], nums[it2] = nums[it2], nums[it1]
                    it1 += 1
                    it2 -= 1
            pivot(l, it2)
            pivot(it1, r)
        pivot(0, len(nums) - 1)
        return nums
