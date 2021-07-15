class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] == 0 and arr[i] == 0:
                    return True
                if arr[j] != 0 and arr[i] == 0:
                    continue
                if arr[j] < 0 and arr[i] < 0:
                    if arr[i] / arr[j] == 2:
                        return True
                if arr[j] > 0 and arr[i] > 0:
                    if arr[j] / arr[i] == 2:
                        return True
        return False
