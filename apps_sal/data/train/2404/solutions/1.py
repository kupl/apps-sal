class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        index = 0
        while (k > 0):
            counter += 1
            if index < len(arr) and arr[index] == counter:
                index += 1
            else:
                k -= 1
        return counter
