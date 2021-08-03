class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        i = len(arr)
        for j in range(0, i):
            for k in range(0, i):
                if(arr[j] > 0 and arr[k] > 0 and arr[j] > arr[k]):
                    if(arr[j] == arr[k] * 2):
                        return True
                elif(arr[j] < 0 and arr[k] < 0 and arr[j] < arr[k]):
                    if(arr[k] * 2 == arr[j]):
                        return True
        if(arr[j] == 0 and arr[k] == 0):
            return True
        else:
            return False
