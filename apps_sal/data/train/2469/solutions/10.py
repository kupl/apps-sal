class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] != 0 and arr[j] / arr[i] == 2):
                    return True
                if(arr[i] == 0 and arr[j] == 0):
                    return True
                if(arr[i] < 0 and arr[j] < 0 and arr[i] / arr[j] == 2):
                    return True
