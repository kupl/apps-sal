class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(len(target)):
            if target[i] != arr[i]:
                if target[i] not in arr[i:]:
                    return False
                else:
                    j = arr[i:].index(target[i]) + len(arr[:i])
                    arr[i], arr[j] = arr[j], arr[i]
        return True
