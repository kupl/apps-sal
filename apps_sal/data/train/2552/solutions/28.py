class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for ar in arr:
            a = self.find(arr, ar,True)
            b = self.find(arr, ar,False)
            if (b - a + 1) > len(arr) * 0.25:
                return ar

    def find(self, arr, value, fromLeft: bool):
        left = 0
        right = len(arr) - 1

        index = -1

        while left <= right:
            mid = (left + right) // 2
            midValue = arr[mid]

            if midValue == value:
                index = mid
                break

            if value < midValue:
                right = mid
            else:
                left = mid


        if fromLeft:
            while index > 0:
                if arr[index] == arr[index-1]:
                    index -= 1
                else:
                    break

            return index
        else:
            while index < (len(arr)-1):
                if arr[index] == arr[index + 1]:
                    index += 1
                else:
                    break


            return index
