class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(len(target)):
            for j in range(i, len(target)):
                if arr[j] == target[i]:
                    break
            else:
                return False
            arr[i:j + 1] = reversed(arr[i:j + 1])
        return arr == target
