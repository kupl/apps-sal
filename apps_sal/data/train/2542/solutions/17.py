class Solution:

    def isMonotonic(self, arr: List[int]) -> bool:
        length = len(arr)
        dec = inc = 1
        for i in range(length - 1):
            if arr[i] < arr[i + 1]:
                dec += 1
            elif arr[i] > arr[i + 1]:
                inc += 1
            else:
                dec += 1
                inc += 1
        if dec == length:
            return True
        elif inc == length:
            return True
        else:
            return False
