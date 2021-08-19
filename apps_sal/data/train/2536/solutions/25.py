class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        current_streak = 0
        for i in range(len(arr)):
            current_streak += 1
            # If this is the last element in the current  streak (as the next is
            # different, or we're at the end of the array).
            if i == len(arr) - 1 or arr[i] != arr[i + 1]:
                # If this is a lucky number
                if arr[i] == current_streak:
                    return arr[i]
                current_streak = 0
        return-1
