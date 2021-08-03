class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def devidelist(L: List[int]):
            if len(L) <= 1:
                return L
            mid = len(L) // 2
            left = devidelist(L[0:mid])
            right = devidelist(L[mid:])
            return mergesort(left, right)

        def mergesort(left: List[int], right: List[int]):
            if not left:
                return right
            if not right:
                return left
            lidx = 0
            ridx = 0
            ans = []
            while lidx < len(left) or ridx < len(right):
                if lidx == len(left):
                    ans.append(right[ridx])
                    ridx += 1
                    continue
                if ridx == len(right):
                    ans.append(left[lidx])
                    lidx += 1
                    continue
                if left[lidx] <= right[ridx]:
                    ans.append(left[lidx])
                    lidx += 1
                else:
                    ans.append(right[ridx])
                    ridx += 1
            return ans

        return devidelist(nums)
